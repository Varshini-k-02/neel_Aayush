# Generated by Django 4.1 on 2022-08-25 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='complaint',
            new_name='ticketid',
        ),
    ]