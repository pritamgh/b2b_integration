from ..models import (
    PurchaseOrderHeader,
    PurchaseOrderLine
)
from .serializers import (
    PurchaseOrderHeaderSerializer,
    PurchaseOrderLineSerializer
)

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)


class PurchaseOrderHeaderList(ListAPIView):

    queryset = PurchaseOrderHeader.objects.all()
    serializer_class = PurchaseOrderHeaderSerializer


class PurchaseOrderHeaderCreate(ListCreateAPIView):

    queryset = PurchaseOrderHeader.objects.all()
    serializer_class = PurchaseOrderHeaderSerializer


class PurchaseOrderHeaderUpdate(RetrieveUpdateAPIView):

    queryset = PurchaseOrderHeader.objects.all()
    serializer_class = PurchaseOrderHeaderSerializer
    lookup_field = 'pk'


class PurchaseOrderHeaderDelete(RetrieveDestroyAPIView):

    queryset = PurchaseOrderHeader.objects.all()
    serializer_class = PurchaseOrderHeaderSerializer
    lookup_field = 'pk'


class PurchaseOrderLineCreate(ListCreateAPIView):

    queryset = PurchaseOrderLine.objects.all()
    serializer_class = PurchaseOrderLineSerializer

    def get(self, request, fk, format=None):
        """ when craete a new line send the header id under which we want to create the line """
        try:
            """ retrieve the lines under this header id """
            lines = PurchaseOrderLine.objects.filter(purchase_order_header_id=fk)
            if request.method == 'GET':
                serialized_lines = PurchaseOrderLineSerializer(
                    lines, many=True)
                return Response(serialized_lines.data)
        except lines.DoesNotExist:
            return Response(status=404)


class PurchaseOrderLineUpdate(RetrieveUpdateAPIView):

    queryset = PurchaseOrderLine.objects.all()
    serializer_class = PurchaseOrderLineSerializer
    lookup_field = 'pk'


class PurchaseOrderLineDelete(RetrieveDestroyAPIView):

    queryset = PurchaseOrderLine.objects.all()
    serializer_class = PurchaseOrderLineSerializer
    lookup_field = 'pk'