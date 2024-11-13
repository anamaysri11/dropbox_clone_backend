# dropbox_clone_backend/files/serializers.py

from rest_framework import serializers
from .models import File, UploadedFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'filename', 'content_type', 'uploaded_at', 'file']
        read_only_fields = ['id', 'filename', 'content_type', 'uploaded_at']

    def create(self, validated_data):
        """
        Create and return a new `File` instance, given the validated data.
        """
        return File.objects.create(**validated_data)
