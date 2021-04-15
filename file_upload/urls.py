from django.urls import path
from .views import (
    upload_file, 
    upload_failed_view,
     upload_csv, 
     dataframe_preview,
     select_tags_to_store,
     file_listview
)

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('files/', file_listview, name='file-listview'),
    path('dataframe_preview/<int:pk>/', dataframe_preview, name='dataframe_preview'),

    path('select_tags_to_store/<int:pk>/', select_tags_to_store, name='select_tags_to_store'),
    path('upload_csv/', upload_csv, name='upload_csv'),
    path('upload_failed/', upload_failed_view, name='upload-failed')

]

