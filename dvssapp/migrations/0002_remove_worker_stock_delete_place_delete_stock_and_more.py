# Generated by Django 5.0.1 on 2024-02-08 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvssapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='stock',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
