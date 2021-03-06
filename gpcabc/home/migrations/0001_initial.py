# Generated by Django 4.0.2 on 2022-02-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Registered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_Nuumber', models.CharField(max_length=100000)),
                ('passout', models.CharField(max_length=122, null=True)),
                ('branch', models.CharField(max_length=122, null=True)),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('address_work', models.TextField(null=True)),
                ('permanent_address', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('passout', models.CharField(max_length=122, null=True)),
                ('receipt', models.CharField(max_length=122, null=True)),
                ('branch', models.CharField(max_length=122, null=True)),
                ('email', models.CharField(max_length=122)),
                ('phone1', models.CharField(max_length=12, null=True)),
                ('phone2', models.CharField(max_length=12, null=True)),
                ('birthday', models.DateField(null=True)),
                ('profession', models.CharField(max_length=122, null=True)),
                ('address1', models.TextField(null=True)),
                ('phone3', models.CharField(max_length=12, null=True)),
                ('address2', models.TextField(null=True)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('passout', models.CharField(max_length=122, null=True)),
                ('branch', models.CharField(max_length=122, null=True)),
                ('email', models.CharField(max_length=122)),
                ('phone1', models.CharField(max_length=12, null=True)),
                ('phone2', models.CharField(max_length=12, null=True)),
                ('birthday', models.DateField(null=True)),
                ('profession', models.CharField(max_length=122, null=True)),
                ('address1', models.TextField(null=True)),
                ('phone3', models.CharField(max_length=12, null=True)),
                ('address2', models.TextField(null=True)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
