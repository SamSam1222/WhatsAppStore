# Generated by Django 4.2.16 on 2024-12-27 19:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IDGenie', '0004_comment_thumbs_down_count_comment_thumbs_up_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='disliked_by',
            field=models.ManyToManyField(blank=True, related_name='disliked_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]