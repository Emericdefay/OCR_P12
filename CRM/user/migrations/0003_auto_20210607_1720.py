# flake8: noqa
# Generated by Django 3.2.4 on 2021-06-07 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20210607_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saler',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='support',
            name='user_id',
        ),
        migrations.AddField(
            model_name='saler',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='support',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
