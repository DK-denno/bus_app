# Generated by Django 4.0.2 on 2022-02-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_app', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squad',
            name='date',
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='squad',
            name='seatsBooked',
            field=models.BigIntegerField(default=0),
        ),
    ]
