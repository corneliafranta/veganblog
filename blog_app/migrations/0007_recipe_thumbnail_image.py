# Generated by Django 2.2.7 on 2020-04-29 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_thumbnailimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='thumbnail_image',
            field=models.CharField(default='thumbnail', max_length=512),
            preserve_default=False,
        ),
    ]
