from rest_framework import viewsets, status
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Commodity, Bid
from .serializers import UserSerializer, CommoditySerializer, BidSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Commodity Rental Solution!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user_type = request.data.get('type')
        if user_type not in ['renter', 'lender']:
            return Response({'status': 'error', 'message': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class CommodityViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        category = request.query_params.get('item_category', None)
        if category:
            self.queryset = self.queryset.filter(item_category=category)
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def accept_bid(self, request, pk=None):
        try:
            commodity = self.get_object()
            bid_id = request.data.get('bid_id')
            if not bid_id:
                return Response({'error': 'Bid ID is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            bid = Bid.objects.get(id=bid_id, commodity=commodity)
        except ObjectDoesNotExist:
            return Response({'error': 'Bid not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update commodity status and details
        commodity.status = 'rented'
        commodity.accepted_bid_price = bid.bid_price_month
        commodity.accepted_rented_period = bid.rental_duration
        commodity.save()

        return Response({'status': 'success', 'message': 'Bid accepted'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def my_commodities(self, request):
        user = request.user
        commodities = Commodity.objects.filter(user=user)
        serializer = self.get_serializer(commodities, many=True)
        return Response({'status': 'success', 'message': 'Commodities fetched successfully', 'payload': serializer.data})

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        commodity = serializer.validated_data['commodity']
        if commodity.status != 'available':
            raise serializers.ValidationError("Commodity is not available for bidding.")
        if serializer.validated_data['bid_price_month'] < commodity.quote_price_per_month:
            raise serializers.ValidationError("Bid price must be higher than the quoted price.")
        serializer.save()

    def list(self, request, *args, **kwargs):
        commodity_id = self.kwargs.get('commodity_id')
        if commodity_id:
            self.queryset = self.queryset.filter(commodity_id=commodity_id)
        return super().list(request, *args, **kwargs)

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )
        return user

@api_view(['POST'])
def user_signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success', 'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)