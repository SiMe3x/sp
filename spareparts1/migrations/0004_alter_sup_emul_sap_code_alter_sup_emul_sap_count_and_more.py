# Generated by Django 4.1 on 2022-08-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0003_sup_emul'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sup_emul',
            name='sap_code',
            field=models.PositiveIntegerField(blank='true'),
        ),
        migrations.AlterField(
            model_name='sup_emul',
            name='sap_count',
            field=models.PositiveIntegerField(blank='true'),
        ),
        migrations.AlterField(
            model_name='sup_emul',
            name='sap_currency',
            field=models.CharField(blank='true', max_length=90),
        ),
        migrations.AlterField(
            model_name='sup_emul',
            name='sap_end_point',
            field=models.CharField(blank='true', max_length=90),
        ),
        migrations.AlterField(
            model_name='sup_emul',
            name='sap_name',
            field=models.CharField(blank='true', max_length=90),
        ),
        migrations.AlterField(
            model_name='sup_emul',
            name='sap_price',
            field=models.PositiveIntegerField(blank='true'),
        ),
        migrations.AlterField(
            model_name='sup_emul',
            name='sap_unit',
            field=models.CharField(blank='true', max_length=90),
        ),
        migrations.AlterField(
            model_name='sup_emul',
            name='sap_warehouse',
            field=models.CharField(blank='true', max_length=90),
        ),
    ]
