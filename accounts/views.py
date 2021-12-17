from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from .models import AuctionProduct, Bidder

# Create your views here.
def my_posted_items(request):
    uid = request.user.id
    my_products = AuctionProduct.objects.filter(user_id=uid)
    context = {'products': my_products}
    return render(request, 'accounts/gallery.html', context)

def gallery(request):
    auction_products = AuctionProduct.objects.all()
    context = {'products': auction_products}
    return render(request, 'accounts/gallery.html', context)

def user_registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user_name}')
            return redirect('gallery')

    
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)

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

def create_auction_product(request):
    return render(request, 'accounts/auction_product_form.html')

def product_details(request, pk):
    product = AuctionProduct.objects.get(id=pk)
    bidders = Bidder.objects.filter(auction_product_id=pk)
    context = {
        'product': product,
        'bidders': bidders
    }
    return render(request, 'accounts/product_details.html', context)