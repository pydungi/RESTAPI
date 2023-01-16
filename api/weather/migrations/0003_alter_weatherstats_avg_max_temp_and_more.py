# Generated by Django 4.1.1 on 2022-12-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_remove_weather_id_remove_weatherstats_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherstats',
            name='avg_max_temp',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='weatherstats',
            name='avg_min_temp',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='weatherstats',
            name='total_rain',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]