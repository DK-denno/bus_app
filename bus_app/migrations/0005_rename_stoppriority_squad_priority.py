# Generated by Django 4.0.2 on 2022-02-27 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bus_app', '0004_squad_stoppriority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squad',
            old_name='stopPriority',
            new_name='priority',
        ),
    ]