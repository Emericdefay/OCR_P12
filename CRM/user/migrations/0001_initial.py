# Generated by Django 3.2.4 on 2021-06-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalerTHROUGH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('client_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SupportTHROUGH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('evend_id', models.IntegerField()),
            ],
        ),
    ]
