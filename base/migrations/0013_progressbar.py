# Generated by Django 4.1 on 2022-08-26 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_admincomp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=400)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticketid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.complaint')),
            ],
        ),
    ]
