from rest_framework import serializers
from .models import Character, House, Title


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    titles = TitleSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'