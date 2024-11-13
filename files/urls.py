# dropbox_clone_backend/files/urls.py

from django.urls import path
from .views import (
    FileUploadView, FileListView, FileDownloadView,
    FileDetailView, FileDeleteView
)

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
    path('files/<int:pk>/delete/', FileDeleteView.as_view(), name='file-delete'),
    path('download/<int:pk>/', FileDownloadView.as_view(), name='file-download'),
]
