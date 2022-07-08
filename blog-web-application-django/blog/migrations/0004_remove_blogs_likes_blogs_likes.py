# Generated by Django 4.0.5 on 2022-07-07 09:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_remove_blogs_likes_blogs_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='likes',
        ),
        migrations.AddField(
            model_name='blogs',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
