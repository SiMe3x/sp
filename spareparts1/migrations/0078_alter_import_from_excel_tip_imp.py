# Generated by Django 4.1 on 2023-10-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0077_alter_import_from_excel_naimen_imp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import_from_excel',
            name='tip_imp',
            field=models.CharField(max_length=190, null='true'),
        ),
    ]
