# Generated by Django 5.0.6 on 2024-06-19 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_title_todos_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todos',
        ),
    ]
