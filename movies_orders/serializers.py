from rest_framework import serializers
from .models import MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source="movie.title", read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    purchased_by = serializers.CharField(source="user.email", read_only=True)
    purchased_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)
