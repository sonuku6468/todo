# Generated by Django 3.2 on 2023-09-07 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20230907_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='complete',
            new_name='completed',
        ),
    ]
