from django.conf.urls import url, include
from .views import AuthRegister, AuthLogin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    
    # url(r'^login/$', AuthLogin.as_view()),
    # url(r'^register/$', AuthRegister.as_view()),

    url(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
]
