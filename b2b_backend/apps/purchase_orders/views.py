from .models import (
    PurchaseOrderHeader,
    PurchaseOrderLine
)

from .api.serializers import (
    PurchaseOrderHeaderSerializer,
    PurchaseOrderLineSerializer
)

from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view(["GET"])
def viewPurchaseOrderHeaderList(request):

    if 'pod_header' in cache:
        # get results from cache
        pod_header_list = cache.get('pod_header')
        return Response(pod_header_list, status=status.HTTP_201_CREATED)

    else:
        pod_header_list = PurchaseOrderHeader.objects.all()
        results = PurchaseOrderHeaderSerializer(pod_header_list, many=True)
        # store data in cache
        pod_header = None
        cache.set(pod_header, results.data, timeout=CACHE_TTL)
        return Response(results.data)


@api_view(["GET"])
def viewPurchaseOrderLineList(request, pk):

    if 'pod_line' in cache:
        # get results from cache
        pod_line_list = cache.get('pod_header_line')
        return Response(pod_line_list, status=status.HTTP_201_CREATED)

    else:
        try:
            pod_line_list = PurchaseOrderLine.objects.filter(
                purchase_order_header_id=pk).order_by('-price')
        except pod_line_list.DoesNotExist:
            return Response(status=404)

        results = PurchaseOrderLineSerializer(pod_line_list, many=True)
        pod_line = None
        cache.set(pod_line, results.data, timeout=CACHE_TTL)
        return Response(results.data)
