# Generated by Django 2.2.16 on 2022-06-20 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220620_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
    ]