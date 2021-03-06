# Generated by Django 2.2.7 on 2020-04-30 21:45

import blog_app.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_product_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, storage=blog_app.storage.OverwriteStorage(), upload_to='C:\\Users\\frant\\PycharmProjects\\veganBlog\\media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, storage=blog_app.storage.OverwriteStorage(), upload_to='C:\\Users\\frant\\PycharmProjects\\veganBlog\\media'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=blog_app.storage.OverwriteStorage(), upload_to='C:\\Users\\frant\\PycharmProjects\\veganBlog\\media'),
        ),
    ]
