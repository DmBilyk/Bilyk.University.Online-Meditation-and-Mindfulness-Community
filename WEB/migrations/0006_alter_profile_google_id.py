# Generated by Django 5.0.3 on 2024-03-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0005_rename_profile_id_profile_google_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='google_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
