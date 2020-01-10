from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from groups.api.serializer import GroupSerializer
from common.api.permissions import IsOwnerOrReadOnly
from common.api.pagination import DefaultPagination
from core.models import Group


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Group.objects.all()
        area = int(self.request.query_params.get('area')
                   ) if self.request.query_params.get('area') else 0
        category = int(self.request.query_params.get('category')
                   ) if self.request.query_params.get('category') else 0

        if area > 0:
            queryset = queryset.filter(area=area)

        if category > 0:
            queryset = queryset.filter(category=category)

        return queryset
