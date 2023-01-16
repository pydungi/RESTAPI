from django.urls import path
from .views import WeatherList, WeatherStatsList
from . import views

urlpatterns = [
    path('weather/', WeatherList.as_view(), name='weather'),
    path('weather/stats/', WeatherStatsList.as_view(), name='weatherstats'),
]