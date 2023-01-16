from rest_framework import generics
from .serializers import YieldSerializer
#from .paginations import CustomPagination
from .models import Yield

# Create your views here.
class YieldList(generics.ListAPIView):

    serializer_class = YieldSerializer
    #pagination_class = CustomPagination
   # filter_backends = [filters.SearchFilter]
   # search_fields = ['year']
    queryset = Yield.objects.all()
