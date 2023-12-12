# Generated by Django 3.2.22 on 2023-12-09 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0013_poll_pollanswer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poll',
            options={'ordering': ['-due_date']},
        ),
        migrations.AddField(
            model_name='poll',
            name='asked_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='forum.category'),
            preserve_default=False,
        ),
    ]