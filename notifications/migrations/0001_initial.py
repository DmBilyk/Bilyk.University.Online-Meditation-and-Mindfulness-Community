# Generated by Django 5.0.3 on 2024-06-04 19:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(choices=[('long_time_no_see', "You haven't visited us for a long time"), ('new_feature', 'We have a new feature out, try it'), ('new_challenge', 'We have a new unique weekly challenge, join us')], max_length=20)),
                ('template', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(choices=[('long_time_no_see', "You haven't visited us for a long time"), ('new_feature', 'We have a new feature out, try it'), ('new_challenge', 'We have a new unique weekly challenge, join us')], max_length=20)),
                ('is_sent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
