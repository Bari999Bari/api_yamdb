# Generated by Django 2.2.16 on 2022-06-23 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220621_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='created',
            new_name='pub_date',
        ),
    ]
