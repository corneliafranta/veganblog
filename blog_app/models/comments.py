from django.db import models
from django.utils import timezone
from django.urls import reverse

class Comments(models.Model):
    post =models.ForeignKey('blog_app.Post', related_name='comments', on_delete=True)
    author = models.CharField(max_length=300)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approved(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
