# Generated by Django 4.1 on 2023-01-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0019_rename_sap_count_spare_part_sap_count_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spare_part',
            name='sap_count_total',
            field=models.PositiveIntegerField(blank='true', default=0),
        ),
    ]
