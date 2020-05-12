from django.db import models
from django.conf import settings
from blog_app.storage import OverwriteStorage

class ThumbnailImage(models.Model):
    thumbnail_name = models.CharField(max_length=512)
    thumbnail_image = models.ImageField(upload_to=settings.MEDIA_ROOT, storage=OverwriteStorage())