from django.conf.urls import url
from . import views
from . import search

urlpatterns = [

    # Purchase Order Header

    url(r'^header-list/$', views.viewPurchaseOrderHeaderList,
        name='purchase_order_header'),

    url(r'^header_id=(?P<pk>[0-9]+)/line-list/$',
        views.viewPurchaseOrderLineList, name='purchase_order_line'),

    url(r'^search/$',
        search.viewSearch, name='search'),
]
