from .models import Yield
from rest_framework import serializers

class YieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yield
        fields = "__all__"
