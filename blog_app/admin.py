from django.contrib import admin
from blog_app.models import Post, Comments, Recipe
# Register your models here.

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Recipe)