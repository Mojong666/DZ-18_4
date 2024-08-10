from django.contrib import admin
from django.urls import path
from task4.views import index_view, shop_view, cart_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
]
