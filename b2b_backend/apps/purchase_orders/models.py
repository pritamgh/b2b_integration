from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone should in the format:'+999999999'.Upto 15 digits allowed.")


class PurchaseOrderHeader(models.Model):

    header_id = models.AutoField(primary_key=True)
    edi_id = models.CharField(
        max_length=60,
        verbose_name=_('EDI ID'),
        help_text=_('Electronic Data Exchange Between Two Tables'),
        null=True,
        blank=True
    )  # Electronic Data Exchange
    order_number = models.CharField(
        max_length=240,
        verbose_name=_('Order Number'),
        null=False,
        blank=False,
    )
    order_date = models.DateTimeField(
        verbose_name=_('Order Date'),
        null=True,
        blank=True,
    )
    order_type = models.CharField(
        max_length=240,
        verbose_name=_('Order Type'),
        null=True,
        blank=True,
    )
    currency = models.DecimalField(
        verbose_name=_('Currency'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    payment_term = models.CharField(
        max_length=240,
        verbose_name=_('Payment Term'),
        null=True,
        blank=True,
    )
    payment_term_text = models.CharField(
        max_length=500,
        verbose_name=_('Payment Term Text'),
        null=True,
        blank=True,
    )
    customer = models.CharField(
        max_length=240,
        verbose_name=_('Customer'),
        null=True,
        blank=True,
    )
    supplier = models.CharField(
        max_length=240,
        verbose_name=_('Supplier'),
        null=False,
        blank=False,
    )
    ship_to_site = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site'),
        null=False,
        blank=False,
    )
    ship_from_site = models.CharField(
        max_length=240,
        verbose_name=_('Ship From Site'),
        null=False,
        blank=False,
    )
    freight_term = models.CharField(
        max_length=240,
        verbose_name=_('Freight Term'),
        null=True,
        blank=True,
    )
    freight_term_meaning = models.CharField(
        max_length=240,
        verbose_name=_('Freight Term Meaning'),
        null=True,
        blank=True,
    )
    freight_carrier = models.CharField(
        max_length=240,
        verbose_name=_('Freight Carrier'),
        null=True,
        blank=True,
    )
    buyer_notes_header = models.CharField(
        max_length=240,
        verbose_name=_('Buyer Notes For Header'),
        null=True,
        blank=True,
    )
    supplier_notes_header = models.CharField(
        max_length=240,
        verbose_name=_('Supplier Notes For Header'),
        null=True,
        blank=True,
    )
    buyer_name = models.CharField(
        max_length=240,
        verbose_name=_('Buyer Name'),
        null=True,
        blank=False,
    )
    buyer_email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        null=True,
        blank=True,
        error_messages={
            'unique': _("A Buyer with this email already exists."),
        },
    )
    buyer_contact = models.CharField(
        validators=[phone_regex],
        max_length=17,
        null=True,
        blank=True,
        verbose_name=_('Buyer Email')
    )
    item = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    item_description_free_form = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    uom = models.CharField(
        max_length=240,
        verbose_name=_('Units of Measure'),
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        verbose_name=_('Price'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    quantity = models.DecimalField(
        verbose_name=_('Product Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    req_delivery_date = models.DateTimeField(
        verbose_name=_('Request Delivery Date'),
        null=True,
        blank=True,
    )
    supplier_suggested_price = models.DecimalField(
        verbose_name=_('Supplier Suggested Price'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    buyer_notes_line = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    supplier_notes_line = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    line_shipped_quantity = models.DecimalField(
        verbose_name=_('Line Shipped Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    line_received_quantity = models.DecimalField(
        verbose_name=_('Line Received Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    line_billed_quantity = models.DecimalField(
        verbose_name=_('Line Billed Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    schedule_num = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    scheduled_quantity = models.DecimalField(
        verbose_name=_('Schedule Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    scheduled_delivery_date = models.DateTimeField(
        verbose_name=_('Scheduled Delivery Date'),
        null=True,
        blank=True,
    )
    promised_delivery_date = models.DateTimeField(
        verbose_name=_('Promised Delivery Date'),
        null=True,
        blank=True,
    )
    quantity_promised = models.DecimalField(
        verbose_name=_('Promised Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    buyer_notes_schedule = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    supplier_notes_schedule = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    quantity_received = models.DecimalField(
        verbose_name=_('Received Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    quantity_shipped = models.DecimalField(
        verbose_name=_('Shipped Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    action = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    ID = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    ship_to_site_name = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site Name'),
        null=True,
        blank=True,
    )
    ship_to_site_address1 = models.TextField(
        verbose_name=_('Shipping Site Address1'),
        null=True,
        blank=True,
    )
    ship_to_site_address2 = models.TextField(
        verbose_name=_('Shipping Site Address2'),
        null=True,
        blank=True,
    )
    ship_to_site_city = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site City'),
        null=True,
        blank=True,
    )
    ship_to_site_state = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site State'),
        null=True,
        blank=True,
    )
    ship_to_site_postalcode = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site PostalCode'),
        null=True,
        blank=True,
    )
    ship_to_site_country = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site Country'),
        null=True,
        blank=True,
    )
    total_lines = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    order_lines_quantity_sum = models.DecimalField(
        verbose_name=_('Order Lines Quantity Summation'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    schedule_status = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    erp_header_id = models.CharField(
        max_length=240,
        verbose_name=_('ERP Header ID'),
        null=True,
        blank=True,
    )
    erp_line_id = models.CharField(
        max_length=240,
        verbose_name=_('ERP Line ID'),
        null=True,
        blank=True,
    )
    erp_schedule_id = models.CharField(
        max_length=240,
        verbose_name=_('ERP Schedule ID'),
        null=True,
        blank=True,
    )
    bill_to_site_name = models.CharField(
        max_length=240,
        verbose_name=_('Bill To Site Name'),
        null=True,
        blank=True,
    )
    bill_to_site_address1 = models.TextField(
        verbose_name=_('Billing Site Address1'),
        null=True,
        blank=True,
    )
    bill_to_site_address2 = models.TextField(
        verbose_name=_('Billing Site Address2'),
        null=True,
        blank=True,
    )
    bill_to_site_city = models.CharField(
        max_length=240,
        verbose_name=_('Bill To Site City'),
        null=True,
        blank=True,
    )
    bill_to_site_state = models.CharField(
        max_length=240,
        verbose_name=_('Bill To Site State'),
        null=True,
        blank=True,
    )
    bill_to_site_postalcode = models.CharField(
        max_length=240,
        verbose_name=_('Bill To SIte PostalCode'),
        null=True,
        blank=True,
    )
    bill_to_site_country = models.CharField(
        max_length=240,
        verbose_name=_('Bill To Site Country'),
        null=True,
        blank=True,
    )
    supplier_item_number = models.PositiveIntegerField(
        verbose_name=_('Supplier Item Number'),
        null=True,
        blank=True,
    )
    manufacturer = models.CharField(
        max_length=240,
        verbose_name=_('MANUFACTURER'),
        null=True,
        blank=True,
    )
    flex_field1 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field2 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field3 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field4 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field5 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field6 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field7 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field8 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field9 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field10 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    supplier_name = models.CharField(
        max_length=240,
        verbose_name=_('Supplier Name'),
        null=True,
        blank=True,
    )
    line_value = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    order_value = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    customer_erp_item_id = models.CharField(
        max_length=240,
        verbose_name=_('Customer ERP Item ID'),
        null=True,
        blank=True,
    )
    supplier_erp_item_id = models.CharField(
        max_length=240,
        verbose_name=_('Supplier ERP Item ID'),
        null=True,
        blank=True,
    )
    sales_order_number = models.PositiveIntegerField(
        verbose_name=_('Sales Order Number'),
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=100,
        verbose_name=_('Status'),
        null=True,
        blank=True,
    )
    status_message = models.TextField(
        verbose_name=_('Status Message'),
        null=True,
        blank=True,
    )
    creation_date = models.DateTimeField(
        verbose_name=_('Date of Creation'),
        null=True,
        blank=True,
    )
    created_by = models.CharField(
        max_length=240,
        verbose_name=_('Created By'),
        null=True,
        blank=True,
    )
    last_update_date = models.DateTimeField(
        verbose_name=_('Last Update Date'),
        null=True,
        blank=True,
    )
    last_updated_by = models.CharField(
        max_length=240,
        verbose_name=_('Last Updated By'),
        null=True,
        blank=True,
    )
    last_user = models.CharField(
        max_length=240,
        verbose_name=_('Last User'),
        null=True,
        blank=True,
    )
    network_id = models.CharField(
        max_length=240,
        verbose_name=_('Network ID'),
        null=True,
        blank=True,
    )
    supplier_id = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    customer_id = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    ship_mode = models.CharField(
        max_length=240,
        verbose_name=_('Shippment Mode'),
        null=True,
        blank=True,
    )
    order_source = models.CharField(
        max_length=240,
        verbose_name=_('Source of Order'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{s.header_id} @ {s.network_id}'.format(s=self)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

##########################


class PurchaseOrderLine(models.Model):

    line_id = models.AutoField(primary_key=True)
    purchase_order_header_id = models.ForeignKey(
        PurchaseOrderHeader,
        on_delete=models.CASCADE,
    )
    edi_id = models.CharField(
        max_length=60,
        verbose_name=_('EDI ID'),
        help_text=_('Electronic Data Exchange Between Two Tables'),
        null=True,
        blank=True
    )  # Electronic Data Exchange
    order_number = models.CharField(
        max_length=240,
        verbose_name=_('Order Number'),
        null=False,
        blank=False,
    )
    order_date = models.DateTimeField(
        verbose_name=_('Order Date'),
        null=True,
        blank=True,
    )
    order_type = models.CharField(
        max_length=240,
        verbose_name=_('Order Type'),
        null=True,
        blank=True,
    )
    currency = models.DecimalField(
        verbose_name=_('Currency'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    payment_term = models.CharField(
        max_length=240,
        verbose_name=_('Payment Term'),
        null=True,
        blank=True,
    )
    payment_term_text = models.CharField(
        max_length=500,
        verbose_name=_('Payment Term Text'),
        null=True,
        blank=True,
    )
    customer = models.CharField(
        max_length=240,
        verbose_name=_('Customer'),
        null=True,
        blank=True,
    )
    supplier = models.CharField(
        max_length=240,
        verbose_name=_('Supplier'),
        null=False,
        blank=False,
    )
    ship_to_site = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site'),
        null=False,
        blank=False,
    )
    ship_from_site = models.CharField(
        max_length=240,
        verbose_name=_('Ship From Site'),
        null=False,
        blank=False,
    )
    freight_term = models.CharField(
        max_length=240,
        verbose_name=_('Freight Term'),
        null=True,
        blank=True,
    )
    freight_term_meaning = models.CharField(
        max_length=240,
        verbose_name=_('Freight Term Meaning'),
        null=True,
        blank=True,
    )
    freight_carrier = models.CharField(
        max_length=240,
        verbose_name=_('Freight Carrier'),
        null=True,
        blank=True,
    )
    buyer_notes_header = models.CharField(
        max_length=240,
        verbose_name=_('Buyer Notes For Header'),
        null=True,
        blank=True,
    )
    supplier_notes_header = models.CharField(
        max_length=240,
        verbose_name=_('Supplier Notes For Header'),
        null=True,
        blank=True,
    )
    buyer_name = models.CharField(
        max_length=240,
        verbose_name=_('Buyer Name'),
        null=True,
        blank=False,
    )
    buyer_email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        null=True,
        blank=True,
        error_messages={
            'unique': _("A Buyer with this email already exists."),
        },
    )
    buyer_contact = models.CharField(
        validators=[phone_regex],
        max_length=17,
        null=True,
        blank=True,
        verbose_name=_('Buyer Email')
    )
    item = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    item_description_free_form = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    uom = models.CharField(
        max_length=240,
        verbose_name=_('Units of Measure'),
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        verbose_name=_('Price'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    quantity = models.DecimalField(
        verbose_name=_('Product Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    req_delivery_date = models.DateTimeField(
        verbose_name=_('Request Delivery Date'),
        null=True,
        blank=True,
    )
    supplier_suggested_price = models.DecimalField(
        verbose_name=_('Supplier Suggested Price'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    buyer_notes_line = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    supplier_notes_line = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    line_shipped_quantity = models.DecimalField(
        verbose_name=_('Line Shipped Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    line_received_quantity = models.DecimalField(
        verbose_name=_('Line Received Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    line_billed_quantity = models.DecimalField(
        verbose_name=_('Line Billed Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    schedule_num = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    scheduled_quantity = models.DecimalField(
        verbose_name=_('Schedule Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    scheduled_delivery_date = models.DateTimeField(
        verbose_name=_('Scheduled Delivery Date'),
        null=True,
        blank=True,
    )
    promised_delivery_date = models.DateTimeField(
        verbose_name=_('Promised Delivery Date'),
        null=True,
        blank=True,
    )
    quantity_promised = models.DecimalField(
        verbose_name=_('Promised Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    buyer_notes_schedule = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    supplier_notes_schedule = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    quantity_received = models.DecimalField(
        verbose_name=_('Received Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    quantity_shipped = models.DecimalField(
        verbose_name=_('Shipped Quantity'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    action = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    ID = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    ship_to_site_name = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site Name'),
        null=True,
        blank=True,
    )
    ship_to_site_address1 = models.TextField(
        verbose_name=_('Shipping Site Address1'),
        null=True,
        blank=True,
    )
    ship_to_site_address2 = models.TextField(
        verbose_name=_('Shipping Site Address2'),
        null=True,
        blank=True,
    )
    ship_to_site_city = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site City'),
        null=True,
        blank=True,
    )
    ship_to_site_state = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site State'),
        null=True,
        blank=True,
    )
    ship_to_site_postalcode = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site PostalCode'),
        null=True,
        blank=True,
    )
    ship_to_site_country = models.CharField(
        max_length=240,
        verbose_name=_('Ship To Site Country'),
        null=True,
        blank=True,
    )
    total_lines = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    order_lines_quantity_sum = models.DecimalField(
        verbose_name=_('Order Lines Quantity Summation'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    schedule_status = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    erp_header_id = models.CharField(
        max_length=240,
        verbose_name=_('ERP Header ID'),
        null=True,
        blank=True,
    )
    erp_line_id = models.CharField(
        max_length=240,
        verbose_name=_('ERP Line ID'),
        null=True,
        blank=True,
    )
    erp_schedule_id = models.CharField(
        max_length=240,
        verbose_name=_('ERP Schedule ID'),
        null=True,
        blank=True,
    )
    bill_to_site_name = models.CharField(
        max_length=240,
        verbose_name=_('Bill To Site Name'),
        null=True,
        blank=True,
    )
    bill_to_site_address1 = models.TextField(
        verbose_name=_('Billing Site Address1'),
        null=True,
        blank=True,
    )
    bill_to_site_address2 = models.TextField(
        verbose_name=_('Billing Site Address2'),
        null=True,
        blank=True,
    )
    bill_to_site_city = models.CharField(
        max_length=240,
        verbose_name=_('Bill To Site City'),
        null=True,
        blank=True,
    )
    bill_to_site_state = models.CharField(
        max_length=240,
        verbose_name=_('Bill To Site State'),
        null=True,
        blank=True,
    )
    bill_to_site_postalcode = models.CharField(
        max_length=240,
        verbose_name=_('Bill To SIte PostalCode'),
        null=True,
        blank=True,
    )
    bill_to_site_country = models.CharField(
        max_length=240,
        verbose_name=_('Bill To Site Country'),
        null=True,
        blank=True,
    )
    supplier_item_number = models.PositiveIntegerField(
        verbose_name=_('Supplier Item Number'),
        null=True,
        blank=True,
    )
    manufacturer = models.CharField(
        max_length=240,
        verbose_name=_('MANUFACTURER'),
        null=True,
        blank=True,
    )
    flex_field1 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field2 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field3 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field4 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field5 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field6 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field7 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field8 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field9 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    flex_field10 = models.CharField(
        max_length=240,
        null=True,
        blank=True,
    )
    supplier_name = models.CharField(
        max_length=240,
        verbose_name=_('Supplier Name'),
        null=True,
        blank=True,
    )
    line_value = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    order_value = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    customer_erp_item_id = models.CharField(
        max_length=240,
        verbose_name=_('Customer ERP Item ID'),
        null=True,
        blank=True,
    )
    supplier_erp_item_id = models.CharField(
        max_length=240,
        verbose_name=_('Supplier ERP Item ID'),
        null=True,
        blank=True,
    )
    sales_order_number = models.PositiveIntegerField(
        verbose_name=_('Sales Order Number'),
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=100,
        verbose_name=_('Status'),
        null=True,
        blank=True,
    )
    status_message = models.TextField(
        verbose_name=_('Status Message'),
        null=True,
        blank=True,
    )
    creation_date = models.DateTimeField(
        verbose_name=_('Date of Creation'),
        null=True,
        blank=True,
    )
    created_by = models.CharField(
        max_length=240,
        verbose_name=_('Created By'),
        null=True,
        blank=True,
    )
    last_update_date = models.DateTimeField(
        verbose_name=_('Last Update Date'),
        null=True,
        blank=True,
    )
    last_updated_by = models.CharField(
        max_length=240,
        verbose_name=_('Last Updated By'),
        null=True,
        blank=True,
    )
    last_user = models.CharField(
        max_length=240,
        verbose_name=_('Last User'),
        null=True,
        blank=True,
    )
    network_id = models.CharField(
        max_length=240,
        verbose_name=_('Network ID'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{s.line_id} lineID of {purchase_order_header_id} headerID'.format(s=self)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
