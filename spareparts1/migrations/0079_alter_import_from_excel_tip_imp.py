# Generated by Django 4.1 on 2023-10-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0078_alter_import_from_excel_tip_imp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import_from_excel',
            name='tip_imp',
            field=models.CharField(max_length=189, null='true'),
        ),
    ]
