# Generated by Django 3.2.22 on 2023-12-14 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_auto_20231214_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_reports', to='forum.post'),
        ),
    ]
