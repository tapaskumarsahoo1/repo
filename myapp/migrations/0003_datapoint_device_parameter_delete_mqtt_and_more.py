# Generated by Django 4.2.4 on 2023-08-26 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_mqtt_message_mqtt_do_mqtt_device_id_mqtt_orp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_type', models.CharField(max_length=20)),
                ('param_value', models.JSONField()),
                ('data_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.datapoint')),
            ],
        ),
        migrations.DeleteModel(
            name='Mqtt',
        ),
        migrations.AddField(
            model_name='datapoint',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.device'),
        ),
    ]
