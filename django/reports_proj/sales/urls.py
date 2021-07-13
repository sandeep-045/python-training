from django.urls import path
from .views import *
app_name = 'sales'

urlpatterns=[
    path('',home,name='home'),
    path('list/',SaleListView.as_view(),name='sales'),
    path('detail/<pk>/',SaleDetailView.as_view(),name='detail')
]