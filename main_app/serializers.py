from rest_framework import serializers
from .models import Character, Condition, Accessory


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    accessories = AccessorySerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'
        read_only_fields = ('character',)
