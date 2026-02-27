from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('about/', about_page_view, name='about'),
    path('products/', products_page_view, name='products'),
    path('contact/', contact_page_view, name='contact'),
]