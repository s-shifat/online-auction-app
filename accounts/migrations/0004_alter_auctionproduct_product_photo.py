# Generated by Django 4.0 on 2021-12-16 21:57

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_bidder_auction_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionproduct',
            name='product_photo',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.get_file_name),
        ),
    ]
