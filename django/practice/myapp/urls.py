from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('show/<str:id>',views.show,name="show")
]
