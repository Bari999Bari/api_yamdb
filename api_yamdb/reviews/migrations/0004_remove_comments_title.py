# Generated by Django 2.2.16 on 2022-06-20 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_comments_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='title',
        ),
    ]