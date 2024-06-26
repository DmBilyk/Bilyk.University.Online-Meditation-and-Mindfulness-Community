# Generated by Django 5.0.3 on 2024-04-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0039_remove_video_image_url_remove_video_youtube_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True, default='')),
                ('youtube_link', models.URLField(default='')),
            ],
        ),
    ]
