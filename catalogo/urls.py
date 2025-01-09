from django.urls import path
from .views import home, about, products, guitar_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('products/', products, name='products'),
    path('products/bajoquintos/<int:id>', guitar_detail, name='guitar_detail'),
]
