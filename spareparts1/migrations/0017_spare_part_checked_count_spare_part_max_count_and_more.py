# Generated by Django 4.1 on 2022-11-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0016_alter_spare_part_criticality_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spare_part',
            name='checked_count',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='spare_part',
            name='max_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='spare_part',
            name='min_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
