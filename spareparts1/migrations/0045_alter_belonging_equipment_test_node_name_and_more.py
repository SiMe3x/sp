# Generated by Django 4.1 on 2023-03-29 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0044_modeq_nodeeq_spec_workp_nodesonequipment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='belonging_equipment_test',
            name='node_name',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nodesonequipment',
            name='part_count',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spareparts1.belonging_equipment_test'),
        ),
    ]
