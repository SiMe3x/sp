# Generated by Django 4.1 on 2023-03-28 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0033_rename_model_eq_modeq_work_proc_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belonging_equipment_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criticality', models.PositiveSmallIntegerField(default=0)),
                ('min_count', models.PositiveIntegerField(default=0)),
                ('max_count', models.PositiveIntegerField(default=0)),
                ('in_node_count', models.PositiveIntegerField(default=0)),
                ('belonging_equipment_key_equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spareparts1.modeq')),
                ('belonging_equipment_key_spareparts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spareparts1.spare_part')),
            ],
        ),
    ]
