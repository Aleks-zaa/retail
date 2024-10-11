from rest_framework import serializers

from users.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор создания пользователей"""

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор  пользователей"""
    class Meta:
        model = User
        fields = '__all__'