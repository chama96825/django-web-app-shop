from django.urls import path
from . import views

urlpatterns = [
    # all the url start with cart/, the cart applicaiton 
    # the first one is cart view
    path('', views.cart_summary, name='cart-summary'),

    # the other urls are not accessed, it will be handled by asynch ajax
    path('add/', views.cart_add, name='cart-add'),

    path('delete', views.cart_delete, name='cart-delete'),

    path('update', views.cart_update, name='cart-update'),


]