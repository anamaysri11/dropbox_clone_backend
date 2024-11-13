# dropbox_clone_backend/files/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse, Http404
from .models import File
from .serializers import FileSerializer
from .models import UploadedFile
from django.shortcuts import get_object_or_404
import mimetypes

ALLOWED_CONTENT_TYPES = [
    'image/png',
    'image/jpeg',
    'image/png',
    'image/jpg'
    'application/pdf',
    'text/plain',
]


# class FileUploadView(APIView):
#     def post(self, request, format=None):
#         content_type = request.data['file'].content_type
#         if content_type not in self.ALLOWED_CONTENT_TYPES:
#             return Response(
#                 {'error': 'File type not supported.'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         serializer = FileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(
#                 filename=request.data['file'].name,
#                 content_type=content_type
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploadView(generics.CreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        # Retrieve the uploaded file
        file_obj = self.request.FILES.get('file')
        if not file_obj:
            raise serializers.ValidationError({"error": "No file provided."})

        # Check if the content type is allowed
        content_type = file_obj.content_type
        if content_type not in ALLOWED_CONTENT_TYPES:
            raise serializers.ValidationError({"error": "File type not supported."})

        # Get the filename
        filename = file_obj.name


        # Save the file using the serializer
        serializer.save(
            filename=filename,
            content_type=content_type,
            file=file_obj
        )

class FileListView(generics.ListAPIView):
    """
    API endpoint for listing all files.
    """
    queryset = File.objects.all().order_by('-uploaded_at')
    serializer_class = FileSerializer

class FileDownloadView(APIView):
    """
    API endpoint for downloading files.
    """

    def get(self, request, pk, format=None):
        file_instance = get_object_or_404(File, pk=pk)
        file_handle = file_instance.file.open()
        mime_type, _ = mimetypes.guess_type(file_instance.filename)
        response = HttpResponse(file_handle, content_type=mime_type)
        response['Content-Length'] = file_instance.file.size
        response['Content-Disposition'] = f'attachment; filename="{file_instance.filename}"'
        return response

class FileDetailView(generics.RetrieveAPIView):
    """
    API endpoint for retrieving file details.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDeleteView(generics.DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer