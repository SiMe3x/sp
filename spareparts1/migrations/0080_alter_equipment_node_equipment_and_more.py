# Generated by Django 4.1 on 2023-10-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0079_alter_import_from_excel_tip_imp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='node_equipment',
            field=models.CharField(max_length=291),
        ),
        migrations.AlterField(
            model_name='spare_part',
            name='spare_part_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='spare_part',
            name='type_part',
            field=models.CharField(default='', max_length=189),
        ),
    ]
