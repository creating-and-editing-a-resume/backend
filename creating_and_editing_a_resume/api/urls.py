from api.views import ProfileViewSet
from django.urls import include, path
from djoser.views import TokenCreateView, UserViewSet
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()

router.register("my-profile", ProfileViewSet, basename="my-profile")


urlpatterns = [
    path("", include(router.urls)),
    path("signup/", UserViewSet.as_view({"post": "create"}), name="signup"),
    path("signin/", TokenCreateView.as_view(), name="signin"),
]
