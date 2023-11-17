from api.views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("my-profile", ProfileViewSet, basename="my-profile")
