# Generated by Django 3.1 on 2020-08-29 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]
