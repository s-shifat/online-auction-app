import datetime
import pytz
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, AuctionProductForm, BidderForm
from .models import AuctionProduct, Bidder
from accounts import forms
from .decorators import unauthenticated_user

# Create your views here.

#---Authentication---##########################################################

@unauthenticated_user
def user_registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account was created for {username}')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('gallery')

    context = {'form': form}
    return render(request, 'accounts/registration.html', context)

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gallery')
        else:
            # meaning user doesn't exist
            messages.info(request, 'Username Or Password incorrect!')
    context = {}
    return render(request, 'accounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

################################################################################



#---Internal App Routes---##########################################################

@login_required(login_url='login')
def gallery(request):
    auction_products = AuctionProduct.objects.all()
    context = {'products': auction_products, 'prompt': 'Auction Gallery'}
    return render(request, 'accounts/gallery.html', context)

@login_required(login_url='login')
def my_posted_items(request):
    uid = request.user.id
    my_products = AuctionProduct.objects.filter(user_id=uid).order_by('-date_created')
    context = {'products': my_products, 'prompt': 'My Auction Items'}
    return render(request, 'accounts/gallery.html', context)


@login_required(login_url='login')
def product_details(request, pk):
    product = AuctionProduct.objects.get(id=pk)
    bidders = Bidder.objects.filter(auction_product_id=pk).order_by('-bid_amount')
    winner = bidders.first
    current_user_as_bidder = Bidder.objects.filter(auction_product_id=pk, bidder=request.user)
    tz = pytz.timezone('Asia/Dhaka')
    today =  datetime.datetime.now(tz=tz)
    context = {
        'product': product,
        'bidders': bidders,
        'current_user_as_bidder': current_user_as_bidder,
        'today': today,
        'winner': winner,
    }
    return render(request, 'accounts/product_details.html', context)

##############################################################################



#---Create Routes---############################################################

@login_required(login_url='login')
def create_auction_product(request):
    product_instance = AuctionProduct(user_id=request.user)
    form = AuctionProductForm(instance=product_instance)

    if request.method == 'POST':
        form = AuctionProductForm(request.POST, request.FILES, instance=product_instance)
        if form.is_valid():
            form.save()
            return redirect('my-posted-items')

    context = {'form': form}
    return render(request, 'accounts/auction_product_form.html', context)


@login_required(login_url='login')
def add_bid(request, pk):
    product = AuctionProduct.objects.get(id=pk)
    initial = {
        'bidder': request.user,
        'auction_product_id': product,
        'bid_amount': product.minimum_bid_price
    }
    bidder_form = BidderForm(initial=initial)
    if request.method == 'POST':
        bidder_form = BidderForm(request.POST, initial=initial)
        if bidder_form.is_valid():
            bidder_form.save()
            return HttpResponseRedirect(reverse('product-details', args=[product.id]))
    context = {'form': bidder_form, 'product': product}
    return render(request, 'accounts/add_bid.html', context)

##############################################################################



#---Update and Delete Routes---############################################################

@login_required(login_url='login')
def update_auction_product(request, pk):
    product = AuctionProduct.objects.get(id=pk)
    form = AuctionProductForm(instance=product)
    if request.method == 'POST':
        form = AuctionProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product-details', args=[product.id]))
    context = {'pk': pk, 'form': form}
    return render(request, 'accounts/auction_product_form.html', context)

@login_required(login_url='login')
def delete_auction_product(request, pk):
    product = AuctionProduct.objects.get(id=pk)
    prompt_content = f'"{product.product_name}"'
    if request.method == 'POST':
        product.delete()
        return redirect('my-posted-items')
    context = {'pk': pk, 'product': product, 'presentation': prompt_content}
    return render(request, 'accounts/delete_page.html', context)

@login_required(login_url='login')
def update_bid(request, pk):
    product = AuctionProduct.objects.get(id=pk)
    bid_person = Bidder.objects.get(bidder=request.user, auction_product_id=product)
    form = BidderForm(instance=bid_person)
    if request.method == 'POST':
        form = BidderForm(request.POST, instance=bid_person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product-details', args=[product.id]))
    context = {'pk': pk, 'form': form}
    return render(request, 'accounts/add_bid.html', context)

@login_required(login_url='login')
def delete_bid(request, pk):
    product = AuctionProduct.objects.get(id=pk)
    bid_person = Bidder.objects.get(bidder=request.user, auction_product_id=product)
    prompt_content = f'Your Bid on "{product.product_name}"'
    if request.method == 'POST':
        bid_person.delete()
        return HttpResponseRedirect(reverse('product-details', args=[product.id]))

    context = {'pk': pk, 'product': product, 'presentation': prompt_content}
    return render(request, 'accounts/delete_page.html', context)
    


##############################################################################

#---Admin Only---############################################################

def view_dashboard(request):
    products = AuctionProduct.objects.all()
    bidders = Bidder.objects.all()
    
    context = {'products': products, 'bidders': bidders}
    return render(request, 'accounts/dashboard.html', context)


#############################################################################