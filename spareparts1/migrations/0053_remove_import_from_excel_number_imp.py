# Generated by Django 4.1 on 2023-10-18 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0052_rename_vliyanie_imp_import_from_excel_kritichnost_obor_imp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='import_from_excel',
            name='number_imp',
        ),
    ]
