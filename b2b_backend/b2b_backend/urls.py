from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^index/', include('apps.accounts.urls')),


    # Cache Based View
    url(r'^purchase-orders/',
        include('apps.purchase_orders.urls')),

    # REST-API endpoints
    url(r'^api/purchase-orders/',
        include('apps.purchase_orders.api.urls')),

    url(r'^api/users/',
        include('apps.users.api.urls')),

    url(r'^api/auth/', include('knox.urls')),

]
