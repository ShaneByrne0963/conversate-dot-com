# Generated by Django 3.2.22 on 2023-11-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='edit-me', max_length=30),
            preserve_default=False,
        ),
    ]