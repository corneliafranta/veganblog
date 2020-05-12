from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from blog_app.storage import OverwriteStorage

#CATEGORY OPTIONS FOR RECIPE
CATEGORY_OPTIONS_RE = (
    ('M', 'Main Dish'),
    ('B', 'Breakfast'),
    ('S', 'Side Dish'),
    ('D', 'Dessert'),
    ('C', 'Cake'),
    ('O', 'Other'),
)

class Recipe(models.Model):
    author = models.ForeignKey('auth.User', on_delete=True)
    title = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY_OPTIONS_RE, default='M', max_length=100)
    description = models.TextField(default='so yummy')
    description2 = models.TextField(default=' ')
    ingredients = models.TextField(default=' ')
    text = models.TextField()
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True, storage=OverwriteStorage())

    #image2 = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    #image3 = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    thumbnail_image = models.CharField(max_length=512, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()

        if self.image:
            self.thumbnail_image = self.image.url[:self.image.url.rfind('/')] + '/' + self.thumbnail_image
        self.save()

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title