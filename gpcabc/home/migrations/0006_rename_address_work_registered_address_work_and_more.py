# Generated by Django 4.0.2 on 2022-02-07 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_name_registered_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registered',
            old_name='Address_Work',
            new_name='address_work',
        ),
        migrations.RenameField(
            model_name='registered',
            old_name='Branch',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='registered',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='registered',
            old_name='Passout',
            new_name='passout',
        ),
        migrations.RenameField(
            model_name='registered',
            old_name='Permanent_Address',
            new_name='permanent_address',
        ),
        migrations.RenameField(
            model_name='registered',
            old_name='Serial_Number',
            new_name='serial_Number',
        ),
    ]
