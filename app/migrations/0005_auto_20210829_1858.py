# Generated by Django 3.2.6 on 2021-08-29 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210829_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_followers',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='profile_likes',
        ),
    ]
