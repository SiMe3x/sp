# Generated by Django 4.1 on 2022-08-10 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Equipment_list',
            new_name='Equipment',
        ),
        migrations.RenameModel(
            old_name='Spare_part_list',
            new_name='Spare_part',
        ),
    ]
