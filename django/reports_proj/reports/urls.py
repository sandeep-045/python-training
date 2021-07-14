from django.urls import path
from .views import (
    create_repo_view,
    ReportListView,
    ReportDetailView, 
    render_pdf_view,
    UploadTemplateView,
    csv_upload_view
    )
app_name = 'reports'

urlpatterns=[
    
    path('',ReportListView.as_view(),name='main'),
    path('save/',create_repo_view,name='create-repo'),
    path('from_file/',UploadTemplateView.as_view(),name='from_file'),
    path('upload/',csv_upload_view,name='upload'),
    path('<pk>/',ReportDetailView.as_view(),name='detail'),
    path('<pk>/pdf',render_pdf_view,name='pdf')
    
]





