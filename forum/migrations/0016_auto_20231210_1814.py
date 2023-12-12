# Generated by Django 3.2.22 on 2023-12-10 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0015_pollanswer_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pollanswer',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='poll',
            name='post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='forum.post'),
        ),
    ]