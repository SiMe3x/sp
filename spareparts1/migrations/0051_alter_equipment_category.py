# Generated by Django 4.1 on 2023-07-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0050_import_from_excel_kritichnost_zapch_imp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='category',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
