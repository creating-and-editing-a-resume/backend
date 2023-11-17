from api.serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class ProfileViewSet(generics.RetrieveUpdateAPIView):
    """
    Личный кабинет пользователя.
    """

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
