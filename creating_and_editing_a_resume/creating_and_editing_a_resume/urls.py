from django.contrib import admin
from django.urls import include, path
from djoser.views import UserViewSet, TokenCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", UserViewSet.as_view({'post': 'create'}), name='create-user'),
    path("signin/", TokenCreateView.as_view(), name='get-token'),
    path('user/', include('user.urls')),
]
