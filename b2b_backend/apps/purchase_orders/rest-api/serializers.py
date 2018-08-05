from ..models import PurchaseOrderHeader, PurchaseOrderLine
from rest_framework import serializers


class PurchaseOrderLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrderLine
        fields = ('purchase_order_header_id', 'line_id', 'item', 'uom', 'price', 'quantity', 'req_delivery_date',
        	      'scheduled_delivery_date', 'promised_delivery_date', 'last_user')


class PurchaseOrderHeaderSerializer(serializers.ModelSerializer):

    purchaseOrderLines = PurchaseOrderLineSerializer(read_only=True)

    """ slug generate by ship-to-site and ship-from-site like [kolkata - bangalore] """
    """author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )"""

    class Meta:
        model = PurchaseOrderHeader
        fields = ('header_id', 'order_number', 'order_type', 'payment_term', 'customer',
                  'supplier', 'buyer_name', 'order_date', 'currency',
                  'freight_term', 'ship_to_site', 'ship_from_site', 'purchaseOrderLines')
