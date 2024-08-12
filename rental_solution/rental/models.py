from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('renter', 'Renter'),
        ('lender', 'Lender'),
    )
    user_type = models.CharField(max_length=6, choices=USER_TYPE_CHOICES)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='rental_user_set',  # Changed related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='rental_user_set',  # Changed related_name
        blank=True
    )

# Commodity Model
class Commodity(models.Model):
    ITEM_CATEGORIES = (
        ('Electronic Appliances', 'Electronic Appliances'),
        ('Electronic Accessories', 'Electronic Accessories'),
        ('Furniture', 'Furniture'),
        ('Men’s wear', 'Men’s wear'),
        ('Women’s wear', 'Women’s wear'),
        ('Shoes', 'Shoes'),
    )
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    quote_price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    item_category = models.CharField(max_length=30, choices=ITEM_CATEGORIES)  # Increased max_length
    lender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commodities')
    status = models.CharField(max_length=10, default='listed')

# Bid Model
class Bid(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, related_name='bids')
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    bid_price_month = models.DecimalField(max_digits=10, decimal_places=2)
    rental_duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
