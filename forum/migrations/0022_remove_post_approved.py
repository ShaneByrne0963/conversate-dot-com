# Generated by Django 3.2.22 on 2024-01-03 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0021_remove_profile_penalty_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='approved',
        ),
    ]