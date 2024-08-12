from rest_framework import serializers
from .models import User, Commodity, Bid

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'type', 'email', 'first_name', 'last_name']

class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = ['id', 'item_name', 'item_description', 'quote_price_per_month', 'item_category', 'status', 'accepted_bid_price', 'accepted_rented_period']

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id', 'commodity', 'bid_price_month', 'rental_duration']
