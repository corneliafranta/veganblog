# Generated by Django 2.2.7 on 2020-04-29 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_recipe_thumbnail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail_image',
            field=models.CharField(default='thumbnail', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail_image',
            field=models.CharField(default='thumbnail', max_length=512),
            preserve_default=False,
        ),
    ]
