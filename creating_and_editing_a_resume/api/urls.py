from api.views import ProfileViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()

router.register("my-profile", ProfileViewSet, basename="my-profile")

urlpatterns = [
    path("", include(router.urls)),
]
