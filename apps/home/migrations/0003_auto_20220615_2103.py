# Generated by Django 3.2.13 on 2022-06-15 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220611_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='posts',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
