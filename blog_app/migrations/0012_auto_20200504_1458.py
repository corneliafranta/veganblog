# Generated by Django 2.2.7 on 2020-05-04 12:58

import blog_app.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_auto_20200430_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description2',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='thumbnailimage',
            name='thumbnail_image',
            field=models.ImageField(storage=blog_app.storage.OverwriteStorage(), upload_to='C:\\Users\\frant\\PycharmProjects\\veganBlog\\media'),
        ),
    ]
