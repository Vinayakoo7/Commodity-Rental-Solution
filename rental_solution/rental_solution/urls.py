from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rental.views import UserViewSet, CommodityViewSet, BidViewSet, user_signup
from rental.views import home


urlpatterns = [
    path('signup/', user_signup, name='user_signup'),
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('api/', include('rental.urls')),  # Include app-level URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
