# Generated by Django 4.1 on 2023-10-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0055_alter_import_from_excel_model_obor_imp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import_from_excel',
            name='edin_izm_imp',
            field=models.CharField(max_length=290, null='true'),
        ),
    ]
