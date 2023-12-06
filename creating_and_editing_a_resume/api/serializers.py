from rest_framework import serializers
from user.models.education import Education
from user.models.user import ResumeUser
from user.models.work import EmploymentHistory


class EducationSerializer(serializers.ModelSerializer):
    """Сериализатор для образования."""

    class Meta:
        model = Education
        fields = (
            "university",
            "start_date",
            "end_date",
            "speciality",
            "grade",
        )


class EmploymentHistorySerializer(serializers.ModelSerializer):
    """Сериализатор для опыта работы."""

    class Meta:
        model = EmploymentHistory
        fields = (
            "company",
            "web_page",
            "position",
            "start_date",
            "end_date",
            "responsibilities",
        )


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для личного кабинета пользователя."""

    education = EducationSerializer(many=True, required=False)
    work = EmploymentHistorySerializer(many=True, required=False)

    class Meta:
        model = ResumeUser
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
            "telegram",
            "city",
            "birth_date",
            "education",
            "work",
        )


class ShortProfileSerializer(ProfileSerializer):
    """Короткий сериализатор для личного кабинета пользователя."""

    class Meta(ProfileSerializer.Meta):
        fields = (
            "first_name",
            "last_name",
            "phone",
            "telegram",
            "city",
            "birth_date",
            "education",
            "work",
        )
