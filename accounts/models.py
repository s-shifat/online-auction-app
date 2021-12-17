from django.db import models
from django.contrib.auth.models import User

def get_file_name(instance, filename):
    extension = filename.split('.')[-1]
    if instance.pk:
        return f"images/{instance.pk}.{extension}"

# Create your models here.
class AuctionProduct(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(null=True)
    product_photo = models.ImageField(null=True, blank=True, upload_to=get_file_name)
    minimum_bid_price = models.DecimalField(max_digits=12, decimal_places=2)
    auction_end_date_time = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Bidder(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_product_id = models.ForeignKey(AuctionProduct, on_delete=models.CASCADE, default=None)
    bid_amount = models.DecimalField(max_digits=12, decimal_places=2)
    bid_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder} - {self.auction_product_id}"