# Generated by Django 4.0.1 on 2022-01-20 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='read_not',
            new_name='read',
        ),
    ]
