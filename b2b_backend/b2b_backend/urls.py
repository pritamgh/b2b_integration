from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/admin/'),
    # name='redirect-to-admin'),
    url(r'^admin/', admin.site.urls),


    # Cache Based View
    url(r'^purchase-orders/',
        include('apps.purchase_orders.urls')),

    # REST-API endpoints
    url(r'^api/purchase-orders/',
        include('apps.purchase_orders.api.urls')),

    # url(r'^api/auth/', include(
    #    'rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/',
        include('apps.users.api.urls')),

    url(r'^api/users/',
        include('apps.users.urls')),

]
