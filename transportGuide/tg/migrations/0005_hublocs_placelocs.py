# Generated by Django 3.2.9 on 2022-01-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0004_poribohonroutes'),
    ]

    operations = [
        migrations.CreateModel(
            name='HubLocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hubName', models.CharField(max_length=250)),
                ('geoLocLat', models.FloatField()),
                ('geoLocLon', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceLocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeName', models.CharField(max_length=250)),
                ('geoLocLat', models.FloatField()),
                ('geoLocLon', models.FloatField()),
            ],
        ),
    ]
