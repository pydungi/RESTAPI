from django.urls import path
from .views import YieldList
from . import views

urlpatterns = [
    path('yield/', YieldList.as_view(), name='yield'),

]