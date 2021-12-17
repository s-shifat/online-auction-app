from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('my-posted-items/', views.my_posted_items, name='my-posted-items'),
    path('registration/', views.user_registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create-auction-product/', views.create_auction_product, name='create-auction-product'),
    path('product-details/<str:pk>/', views.product_details, name='product-details')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

