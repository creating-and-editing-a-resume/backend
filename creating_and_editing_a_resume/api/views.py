from api.serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Личный кабинет пользователя.
    """

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "put", "patch"]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
