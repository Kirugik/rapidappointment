# Generated by Django 4.0.5 on 2022-06-23 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_rename_full_name_doctor_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='first_name',
            new_name='first_Name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='last_name',
            new_name='last_Name',
        ),
    ]