# Generated by Django 3.2.22 on 2023-12-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
