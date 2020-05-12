from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from blog_app.storage import OverwriteStorage
#CATEGORY OPTIONS

CATEGORY_OPTIONS = (
    ('RE', 'Recipe'),
    ('NE', 'News'),
    ('ST', 'Standard'),
    ('AD', 'Advertisement'),
    ('IN', 'Information'),
)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=True )
    title = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY_OPTIONS, default='ST', max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to = settings.MEDIA_ROOT, blank=True, storage=OverwriteStorage())
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    thumbnail_image = models.CharField(max_length=512, null=True, blank=True)


    def publish(self):
        self.published_date = timezone.now()
        if self.image:
            self.thumbnail_image = self.image.url[:self.image.url.rfind('/')] + '/' + self.thumbnail_image
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

