# Generated by Django 4.1 on 2023-01-28 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0018_spare_part_sap_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spare_part',
            old_name='sap_count',
            new_name='sap_count_total',
        ),
    ]
