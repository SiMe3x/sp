# Generated by Django 4.1 on 2023-03-09 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0024_alter_spare_part_sap_code2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spare_part',
            name='sap_Code2',
            field=models.PositiveIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='spare_part',
            name='sap_analog',
            field=models.PositiveIntegerField(blank=True, default='0', null=True),
        ),
    ]
