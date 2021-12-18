from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelForm
from .models import AuctionProduct, Bidder
from django.contrib import messages

def is_validated_bid(amount, min_bid):
    return amount >= min_bid

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AuctionProductForm(ModelForm):
    class Meta:
        model = AuctionProduct
        fields = [
            'user_id',
            'product_name',
            'product_description',
            'product_photo',
            'minimum_bid_price',
            'auction_end_date_time',
        ]
        # https://stackoverflow.com/questions/60128838/django-datetimeinput-type-datetime-local-not-saving-to-database
        # https://stackoverflow.com/questions/4945802/how-can-i-disable-a-model-field-in-a-django-form
        widgets = {
            'auction_end_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # 'user_id': forms.Textarea(attrs={'cols': 30, 'rows': 1})
            'user_id': forms.HiddenInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].disabled = True

class BidderForm(ModelForm):
    class Meta:
        model = Bidder
        fields = [
            'bidder',
            'auction_product_id',
            'bid_amount'
        ]
        widgets = {
            'bidder': forms.HiddenInput(),
            'auction_product_id': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bidder'].disabled = True
        self.fields['auction_product_id'].disabled = True

    def clean_bid_amount(self):
        amount = self.cleaned_data.get('bid_amount')
        product_id = self.cleaned_data.get('auction_product_id')
        product = AuctionProduct.objects.get(id=product_id.id)
        min_bid = product.minimum_bid_price

        if not is_validated_bid(amount, min_bid):
            promt = f'Minimum Bid price is {min_bid} BDT' 
            raise forms.ValidationError(promt)

        return amount