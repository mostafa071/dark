# Generated by Django 5.0.6 on 2024-06-18 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todos',
            old_name='title',
            new_name='name',
        ),
    ]
