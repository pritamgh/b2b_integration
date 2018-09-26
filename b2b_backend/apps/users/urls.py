from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'', views.index, name='index'),
    # url(r'^login/$', views.login_view, name='login'),
    # url(r'^logout/$', views.logout_view, name='logout')

    url(r'random-users/', views.GenerateRandomUserView.as_view()),
    # url(r'users_list/', views. name='users_list'),
]
