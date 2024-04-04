from rest_framework import serializers
from .models import Character, Condition, Accessory
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # Add a password field, make it write-only
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            # Ensures the password is hashed correctly
            password=validated_data['password']
        )

        return user


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    accessories = AccessorySerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'
        read_only_fields = ('character',)
