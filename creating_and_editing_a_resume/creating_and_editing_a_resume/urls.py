from django.contrib import admin
from django.urls import include, path
from djoser import views as djoser_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/signup/", djoser_views.UserViewSet.as_view({'post': 'create'}), name='create-user'),
    path("api/v1/signin/", djoser_views.TokenCreateView.as_view(), name='get-token'),
    path('api/v1/', include('user.urls')),
]
