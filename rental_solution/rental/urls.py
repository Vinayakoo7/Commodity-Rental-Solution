from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CommodityViewSet, BidViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'commodities', CommodityViewSet)
router.register(r'bids', BidViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
