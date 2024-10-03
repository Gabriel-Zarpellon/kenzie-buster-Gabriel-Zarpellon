from rest_framework import serializers
from .models import Rating, Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(
        choices=Rating.choices, default=Rating.G, required=False
    )
    synopsis = serializers.CharField(required=False)

    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)
