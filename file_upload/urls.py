from django.urls import path
from .views import (
    upload_file, 
    upload_failed_view,
     upload_csv, 
     dataframe_preview
)

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('dataframe_preview/<int:pk>', dataframe_preview, name='dataframe_preview'),
    path('upload_csv/', upload_csv, name='upload_csv'),
    path('upload_failed/', upload_failed_view, name='upload-failed')

]

