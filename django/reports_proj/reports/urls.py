from django.urls import path
from .views import create_repo_view

app_name = 'reports'

urlpatterns=[
    path('save/',create_repo_view,'create-repo')
]