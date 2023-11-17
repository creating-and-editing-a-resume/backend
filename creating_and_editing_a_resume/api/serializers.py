from rest_framework import serializers
from user.models.user import ResumeUser


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для личного кабинета пользователя."""

    class Meta:
        model = ResumeUser
        fields = "__all__"
