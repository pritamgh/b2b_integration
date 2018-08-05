from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/admin/'), name='redirect-to-admin'),
    url(r'^admin/', admin.site.urls),

    # REST-API endpoints
    url(r'^api/purchase-orders/',
        include('apps.purchase_orders.rest-api.urls')),

    url(r'^$', RedirectView.as_view(url='/api/auth'), name='redirect-to-admin'),
    # url(r'^api/auth/', include(
    #    'rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/',
        include('apps.users.rest-api.urls')),

]
