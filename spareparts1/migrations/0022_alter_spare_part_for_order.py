# Generated by Django 4.1 on 2023-01-28 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0021_alter_spare_part_sap_count_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spare_part',
            name='for_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
