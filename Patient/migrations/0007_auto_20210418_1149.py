# Generated by Django 3.2 on 2021-04-18 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0006_rename_user_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='id',
            new_name='Did',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='id',
            new_name='Uid',
        ),
    ]
