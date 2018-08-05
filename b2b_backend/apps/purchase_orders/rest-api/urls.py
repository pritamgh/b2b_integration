from django.conf.urls import url
from . import views

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # Purchase Order Header

    url(r'^header-list/$', views.PurchaseOrderHeaderList.as_view(),
        name='purchase_order_list'),

    url(r'^create/$', views.PurchaseOrderHeaderCreate.as_view(),
        name='create purchase order header'),

    url(r'^update/header_id=(?P<pk>[0-9]+)/$',
        views.PurchaseOrderHeaderUpdate.as_view(),
        name='update purchase order header'),

    url(r'^delete/header_id=(?P<pk>[0-9]+)/$',
        views.PurchaseOrderHeaderDelete.as_view(),
        name='delete purchase order header'),

    # Purchase Order Line

    # add line under a perticular header where header_id is the foreign key in line table
    url(r'^header_id=(?P<fk>[0-9]+)/add-line/$', views.PurchaseOrderLineCreate.as_view(),
        name='create purchase order line'),

    url(r'^update/line_id=(?P<pk>[0-9]+)/$',
        views.PurchaseOrderLineUpdate.as_view(),
        name='update purchase order line'),

    url(r'^delete/line_id=(?P<pk>[0-9]+)/$',
        views.PurchaseOrderLineDelete.as_view(),
        name='delete purchase order line'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
