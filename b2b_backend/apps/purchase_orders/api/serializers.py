from ..models import PurchaseOrderHeader, PurchaseOrderLine
from rest_framework import serializers


class PurchaseOrderLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrderLine
        fields = ('purchase_order_header_id', 'line_id', 'item',
                  'uom', 'price', 'quantity', 'req_delivery_date',
                  'scheduled_delivery_date', 'promised_delivery_date',
                  'last_user')


class PurchaseOrderHeaderSerializer(serializers.ModelSerializer):

    purchaseOrderLines = PurchaseOrderLineSerializer(read_only=True)

    class Meta:
        model = PurchaseOrderHeader
        # fields = ('header_id', 'order_number', 'order_type', 'payment_term',
        #           'customer', 'supplier', 'buyer_name', 'price', 'quantity',
        #           'order_date', 'currency', 'freight_term', 'ship_to_site',
        #           'ship_from_site', 'purchaseOrderLines')
        fields = ('header_id', 'order_number', 'buyer_name', 'ship_to_site',
                  'ship_from_site', 'purchaseOrderLines')
