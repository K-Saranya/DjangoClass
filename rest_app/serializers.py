from rest_framework import serializers
from .models import *


class ProductsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsInfo
        fields = '__all__'