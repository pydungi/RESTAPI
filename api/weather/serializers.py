from .models import Weather, WeatherStats
from rest_framework import serializers

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = "__all__"

class WeatherStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherStats
        fields = "__all__"