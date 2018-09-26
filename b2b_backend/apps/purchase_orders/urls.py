from django.conf.urls import url
from . import views

urlpatterns = [

    # Purchase Order Header

    url(r'^header-list/$', views.viewPurchaseOrderList,
        name='purchase_order_list'),

    url(r'^header_id=(?P<pk>[0-9]+)/line-list/$',
        views.viewPurchaseOrderHeaderLine, name='purchase_order_header_line'),
]
