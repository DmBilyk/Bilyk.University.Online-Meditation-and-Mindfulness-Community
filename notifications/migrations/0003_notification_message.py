# Generated by Django 5.0.3 on 2024-06-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_remove_notification_user_notification_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
