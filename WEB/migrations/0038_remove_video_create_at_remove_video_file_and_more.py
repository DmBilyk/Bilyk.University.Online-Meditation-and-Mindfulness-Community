# Generated by Django 5.0.4 on 2024-04-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0037_remove_video_image_url_remove_video_youtube_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='video',
            name='file',
        ),
        migrations.RemoveField(
            model_name='video',
            name='image',
        ),
        migrations.AddField(
            model_name='video',
            name='image_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='video',
            name='youtube_link',
            field=models.URLField(default=''),
        ),
    ]
