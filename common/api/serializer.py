from rest_framework import serializers
from core.models import Area, Category


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Area
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = "__all__"