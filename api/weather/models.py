from django.db import models

# Create your models here.
class Weather(models.Model):
    station_id = models.CharField(primary_key=True,max_length=20)
    date = models.DateField()
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()
    rain = models.IntegerField()

    class Meta:
        db_table = 'weather_data'

class WeatherStats(models.Model):
    station_id = models.CharField(primary_key=True, max_length=20)
    year = models.IntegerField()
    avg_min_temp = models.DecimalField(decimal_places=2,max_digits=8)
    avg_max_temp = models.DecimalField(decimal_places=2,max_digits=8)
    total_rain = models.DecimalField(decimal_places=2,max_digits=8)

    class Meta:
        db_table = 'weather_stats'