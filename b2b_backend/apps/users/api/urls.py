from django.conf.urls import url, include
from rest_framework import routers

from .views import (
    UserAPI,
    RegistrationAPI,
    LoginAPI,
    LogoutAPI
)

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/user/$', UserAPI.as_view()),
    url(r'^auth/register/$', RegistrationAPI.as_view()),
    url(r'^auth/login/$', LoginAPI.as_view()),
    url(r'^auth/logout/$', LogoutAPI.as_view()),
]
