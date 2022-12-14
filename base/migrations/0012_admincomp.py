# Generated by Django 4.1 on 2022-08-25 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_complaint_handler'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminComp',
            fields=[
                ('ticketid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('docLink', models.CharField(max_length=1000)),
                ('handler', models.CharField(default=None, max_length=30)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('complainant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
