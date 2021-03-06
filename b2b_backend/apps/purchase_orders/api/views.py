from ..models import (
    PurchaseOrderHeader,
    PurchaseOrderLine
)
from .serializers import (
    PurchaseOrderHeaderSerializer,
    PurchaseOrderLineSerializer
)
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from django_filters import rest_framework as filters


# Filtering Option
class PurchaseOrderHeaderFilter(filters.FilterSet):

    class Meta:
        model = PurchaseOrderHeader
        fields = ['price', 'quantity']


class PurchaseOrderHeaderList(ListAPIView):

    queryset = PurchaseOrderHeader.objects.all()

    permission_classes = [permissions.AllowAny, ]
    serializer_class = PurchaseOrderHeaderSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PurchaseOrderHeaderFilter


class PurchaseOrderHeaderCreate(ListCreateAPIView):

    # queryset = PurchaseOrderHeader.objects.all()

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PurchaseOrderHeaderSerializer

    def get_queryset(self):
        return self.request.user.PurchaseOrderHeader.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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
        """ when craete a new line send the header id under which
        we want to create the line """
        try:
            """ retrieve the lines under this header id """
            lines = PurchaseOrderLine.objects.filter(
                purchase_order_header_id=fk)
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


# Search Functionality
class SearchApiView(ListAPIView):

    queryset = PurchaseOrderHeader.objects.all()
    serializer_class = PurchaseOrderHeaderSerializer
    filter_fields = ('ship_from_site')
