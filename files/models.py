# dropbox_clone_backend/files/models.py

from django.db import models

class File(models.Model):
    """
    Model representing an uploaded file.
    """
    file = models.FileField(upload_to='uploads/')
    filename = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename

# files/models.py


def upload_to(instance, filename):
    # Optionally, customize the upload path
    return f'uploads/{filename}'

class UploadedFile(models.Model):
    filename = models.CharField(max_length=255)
    content_type = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.filename
