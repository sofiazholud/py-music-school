from rest_framework import serializers
from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField()

    class Meta:
        model = Musician
        fields = [
            "first_name",
            "last_name",
            "instrument",
            "age",
            "is_adult"
        ]
