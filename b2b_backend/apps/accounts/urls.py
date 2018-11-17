from django.conf.urls import url, include
# from django.contrib.auth import views

from . import views as accounts_view

urlpatterns = [

    url(r'^$', accounts_view.index, name='index'),
    url(r'^login/$', accounts_view.login_view, name='login'),
    url(r'^logout/$', accounts_view.logout_view, name='logout'),

    # Django's default auth
    # url(r'^login/$', views.login, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),

    url(r'^auth/', include('social_django.urls', namespace='social'))
]
