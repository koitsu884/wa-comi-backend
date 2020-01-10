from rest_framework import viewsets
from core.models import Area, Category
from common.api.serializer import AreaSerializer, CategorySerializer


class AreaListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


