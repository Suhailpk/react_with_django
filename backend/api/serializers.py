from rest_framework.serializers import ModelSerializer
from .models import *


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'start_date', 'end_date', 'comments', 'status')