from rest_framework import serializers

from retail.models import Network


class NetworkSerializer(serializers.ModelSerializer):
    """Сериализатор сети"""
    class Meta:
        model = Network
        fields = '__all__'
        read_only_fields = ('created_at', )
