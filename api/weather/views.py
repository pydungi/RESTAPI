from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import WeatherSerializer, WeatherStatsSerializer
from .paginations import CustomPagination
from .models import Weather, WeatherStats
# Create your views here.

class WeatherList(generics.ListAPIView):

    serializer_class = WeatherSerializer
    pagination_class = CustomPagination
    #filter_backends = [filters.SearchFilter]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['station_id', 'date']
    search_fields = ['station_id', 'date']
    queryset = Weather.objects.all()

    def get_queryset(self):

        queryset = Weather.objects.all()
        station_id = self.request.query_params.get('station_id')
        if station_id is not None:
            queryset = queryset.filter(station_id=station_id)
        return queryset

class WeatherStatsList(generics.ListAPIView):

    serializer_class = WeatherStatsSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['station_id', 'year']
    queryset = WeatherStats.objects.all()
