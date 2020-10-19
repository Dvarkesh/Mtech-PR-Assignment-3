from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import FileUpload

admin.site.register(FileUpload)
# Register your models here.
