# Generated by Django 3.2.4 on 2021-06-07 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210607_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salerthrough',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='salerthrough',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='supportthrough',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='supportthrough',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='supportthrough',
            old_name='user_id',
            new_name='user',
        ),
    ]
