# Generated by Django 3.2.8 on 2021-10-23 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwordmanager', '0005_rename_author_account_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
    ]
