from api.serializers import ProfileSerializer, ShortProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class ProfileViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Личный кабинет пользователя.
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.select_related("educations", "works").filter(
            id=self.request.user.id
        )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProfileSerializer
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return ShortProfileSerializer
