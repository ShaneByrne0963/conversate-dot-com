# Generated by Django 3.2.22 on 2023-12-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20231204_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='fa-tag', max_length=30),
        ),
    ]
