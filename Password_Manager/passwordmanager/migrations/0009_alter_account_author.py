# Generated by Django 3.2.8 on 2021-10-24 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passwordmanager', '0008_alter_account_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
