# Generated by Django 2.2.7 on 2020-04-28 18:02

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('M', 'Main Dish'), ('B', 'Breakfast'), ('S', 'Side Dish'), ('D', 'Dessert'), ('C', 'Cake'), ('O', 'Other')], default='M', max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='C:\\Users\\frant\\PycharmProjects\\veganBlog\\media')),
                ('image2', models.ImageField(blank=True, upload_to='C:\\Users\\frant\\PycharmProjects\\veganBlog\\media')),
                ('image3', models.ImageField(blank=True, upload_to='C:\\Users\\frant\\PycharmProjects\\veganBlog\\media')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('RE', 'Recipe'), ('NE', 'News'), ('ST', 'Standard'), ('AD', 'Advertisement'), ('IN', 'Information')], default='ST', max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='C:\\Users\\frant\\PycharmProjects\\veganBlog\\media')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=True, related_name='comments', to='blog_app.Post')),
            ],
        ),
    ]
