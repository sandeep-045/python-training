from django.urls import path
from tasks import views
urlpatterns = [
    path('',views.home,name='home'),
    path('update/<str:pk>',views.update_task,name='update'),
    path('delete/<str:pk>',views.delete_task,name='delete'),
]
