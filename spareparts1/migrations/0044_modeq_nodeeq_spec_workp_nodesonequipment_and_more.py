# Generated by Django 4.1 on 2023-03-29 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0043_remove_modeq_work_proc_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModEq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_eq_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NodeEq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_eq_name', models.CharField(max_length=90)),
                ('model_eq_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spareparts1.modeq')),
            ],
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_proc_name', models.CharField(max_length=50)),
                ('spec_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spareparts1.spec')),
            ],
        ),
        migrations.CreateModel(
            name='NodesOnEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_count', models.PositiveIntegerField(default=0)),
                ('node_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spareparts1.nodeeq')),
            ],
        ),
        migrations.AddField(
            model_name='modeq',
            name='work_proc_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spareparts1.workp'),
        ),
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
                ('node_name', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='spareparts1.nodesonequipment')),
            ],
        ),
    ]
