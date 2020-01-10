from rest_framework import serializers
from core.models import Group
from user.serializers import UserSerializer
from common.api.serializer import AreaSerializer, CategorySerializer


class GroupSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created_at = serializers.SerializerMethodField()
    area = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    area_id = serializers.IntegerField(write_only=True, required=False)
    category_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model=Group
        exclude = ['updated_at', 'is_active']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_area(self, instance):
        return instance.area.StringRelatedField()