# Generated by Django 4.1 on 2022-08-26 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_progressbar_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progressbar',
            name='commenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
