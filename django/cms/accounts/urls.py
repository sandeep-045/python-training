from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('products',ProductList,name='products'),
    path('',Dashboard,name='dashboard'),
    path('logout',LogoutUser,name='logout'),
    path('customers/<str:pk>',CustomerDetail,name='customers'),
    path('createorder/<str:pk>',CreateOrder,name='create-order'),
    path('updateorder/<str:pk>',UpdateOrder,name='update-order'),
    path('deleteorder/<str:pk>',DeleteOrder,name='delete-order'),
    path('register',RegisterUser,name='register'),
    path('login',LoginUser,name='login'),
    path('user',UserPage,name='user'),
    path('useracc',accountSettings,name='useracc'),
    path('reset_password',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]