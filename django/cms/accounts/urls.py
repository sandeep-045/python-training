from django.urls import path
from accounts.views import *
urlpatterns = [
    
    path('products',ProductList,name='products'),
    path('',Dashboard,name='dashboard'),
    path('customers/<str:pk>',CustomerDetail,name='customers'),
    path('createorder/<str:pk>',CreateOrder,name='create-order'),
    path('updateorder/<str:pk>',UpdateOrder,name='update-order'),
    path('deleteorder/<str:pk>',DeleteOrder,name='delete-order')
]