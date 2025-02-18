# Generated by Django 4.1 on 2023-03-29 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts1', '0034_belonging_equipment_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodesOnEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_count', models.PositiveIntegerField(default=0)),
                ('node_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spareparts1.nodeeq')),
            ],
        ),
        migrations.AddField(
            model_name='belonging_equipment_test',
            name='node_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='spareparts1.nodesonequipment'),
        ),
    ]
