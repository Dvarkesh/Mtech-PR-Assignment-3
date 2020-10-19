from django.db import models

# Create your models here.
class FileUpload(models.Model):
    files = models.FileField(upload_to ="media")
