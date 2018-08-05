# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 05:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrderHeader',
            fields=[
                ('header_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_number', models.CharField(max_length=240, verbose_name='Order Number')),
                ('order_date', models.DateTimeField(blank=True, null=True, verbose_name='Order Date')),
                ('order_type', models.CharField(blank=True, max_length=240, null=True, verbose_name='Order Type')),
                ('currency', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Currency')),
                ('payment_term', models.CharField(blank=True, max_length=240, null=True, verbose_name='Payment Term')),
                ('payment_term_text', models.CharField(blank=True, max_length=500, null=True, verbose_name='Payment Term Text')),
                ('customer', models.CharField(blank=True, max_length=240, null=True, verbose_name='Customer')),
                ('supplier', models.CharField(max_length=240, verbose_name='Supplier')),
                ('ship_to_site', models.CharField(max_length=240, verbose_name='Ship To Site')),
                ('ship_from_site', models.CharField(max_length=240, verbose_name='Ship From Site')),
                ('freight_term', models.CharField(blank=True, max_length=240, null=True, verbose_name='Freight Term')),
                ('freight_term_meaning', models.CharField(blank=True, max_length=240, null=True, verbose_name='Freight Term Meaning')),
                ('freight_carrier', models.CharField(blank=True, max_length=240, null=True, verbose_name='Freight Carrier')),
                ('buyer_notes_header', models.CharField(blank=True, max_length=240, null=True, verbose_name='Buyer Notes For Header')),
                ('supplier_notes_header', models.CharField(blank=True, max_length=240, null=True, verbose_name='Supplier Notes For Header')),
                ('buyer_name', models.CharField(max_length=240, null=True, verbose_name='Buyer Name')),
                ('buyer_email', models.EmailField(blank=True, error_messages={'unique': 'A Buyer with this email already exists.'}, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('buyer_contact', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone should in the format:'+999999999'.Upto 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Buyer Email')),
                ('item', models.CharField(blank=True, max_length=240, null=True)),
                ('item_description_free_form', models.CharField(blank=True, max_length=240, null=True)),
                ('uom', models.CharField(blank=True, max_length=240, null=True, verbose_name='Units of Measure')),
                ('price', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Price')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Product Quantity')),
                ('req_delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='Request Delivery Date')),
                ('supplier_suggested_price', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Supplier Suggested Price')),
                ('buyer_notes_line', models.CharField(blank=True, max_length=240, null=True)),
                ('supplier_notes_line', models.CharField(blank=True, max_length=240, null=True)),
                ('line_shipped_quantity', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Line Shipped Quantity')),
                ('line_received_quantity', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Line Received Quantity')),
                ('line_billed_quantity', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Line Billed Quantity')),
                ('schedule_num', models.PositiveIntegerField(blank=True, null=True)),
                ('scheduled_quantity', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Schedule Quantity')),
                ('scheduled_delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='Scheduled Delivery Date')),
                ('promised_delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='Promised Delivery Date')),
                ('quantity_promised', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Promised Quantity')),
                ('buyer_notes_schedule', models.CharField(blank=True, max_length=240, null=True)),
                ('supplier_notes_schedule', models.CharField(blank=True, max_length=240, null=True)),
                ('quantity_received', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Received Quantity')),
                ('quantity_shipped', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Shipped Quantity')),
                ('action', models.CharField(blank=True, max_length=240, null=True)),
                ('ID', models.PositiveIntegerField(blank=True, null=True)),
                ('ship_to_site_name', models.CharField(blank=True, max_length=240, null=True, verbose_name='Ship To Site Name')),
                ('ship_to_site_address1', models.TextField(blank=True, null=True, verbose_name='Shipping Site Address1')),
                ('ship_to_site_address2', models.TextField(blank=True, null=True, verbose_name='Shipping Site Address2')),
                ('ship_to_site_city', models.CharField(blank=True, max_length=240, null=True, verbose_name='Ship To Site City')),
                ('ship_to_site_state', models.CharField(blank=True, max_length=240, null=True, verbose_name='Ship To Site State')),
                ('ship_to_site_postalcode', models.CharField(blank=True, max_length=240, null=True, verbose_name='Ship To Site PostalCode')),
                ('ship_to_site_country', models.CharField(blank=True, max_length=240, null=True, verbose_name='Ship To Site Country')),
                ('total_lines', models.PositiveIntegerField(blank=True, null=True)),
                ('order_lines_quantity_sum', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Order Lines Quantity Summation')),
                ('schedule_status', models.CharField(blank=True, max_length=240, null=True)),
                ('erp_header_id', models.CharField(blank=True, max_length=240, null=True, verbose_name='ERP Header ID')),
                ('erp_line_id', models.CharField(blank=True, max_length=240, null=True, verbose_name='ERP Line ID')),
                ('erp_schedule_id', models.CharField(blank=True, max_length=240, null=True, verbose_name='ERP Schedule ID')),
                ('bill_to_site_name', models.CharField(blank=True, max_length=240, null=True, verbose_name='Bill To Site Name')),
                ('bill_to_site_address1', models.TextField(blank=True, null=True, verbose_name='Billing Site Address1')),
                ('bill_to_site_address2', models.TextField(blank=True, null=True, verbose_name='Billing Site Address2')),
                ('bill_to_site_city', models.CharField(blank=True, max_length=240, null=True, verbose_name='Bill To Site City')),
                ('bill_to_site_state', models.CharField(blank=True, max_length=240, null=True, verbose_name='Bill To Site State')),
                ('bill_to_site_postalcode', models.CharField(blank=True, max_length=240, null=True, verbose_name='Bill To SIte PostalCode')),
                ('bill_to_site_country', models.CharField(blank=True, max_length=240, null=True, verbose_name='Bill To Site Country')),
                ('supplier_item_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Supplier Item Number')),
                ('manufacturer', models.CharField(blank=True, max_length=240, null=True, verbose_name='MANUFACTURER')),
                ('flex_field1', models.CharField(blank=True, max_length=240, null=True)),
                ('flex_field2', models.CharField(blank=True, max_length=240, null=True)),
                ('flex_field3', models.CharField(blank=True, max_length=240, null=True)),
                ('flex_field4', models.CharField(blank=True, max_length=240, null=True)),
                ('flex_field5', models.CharField(blank=True, max_length=240, null=True)),
                ('flex_field6', models.CharField(blank=True, max_length=240, null=True)),
                ('flex_field7', models.CharField(blank=True, max_length=240, null=True)),
                ('flex_field8', models.CharField(blank=True, max_length=240, null=True)),
                ('flex_field9', models.CharField(blank=True, max_length=240, null=True)),
                ('flex_field10', models.CharField(blank=True, max_length=240, null=True)),
                ('supplier_name', models.CharField(blank=True, max_length=240, null=True, verbose_name='Supplier Name')),
                ('line_value', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('order_value', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('customer_erp_item_id', models.CharField(blank=True, max_length=240, null=True, verbose_name='Customer ERP Item ID')),
                ('supplier_erp_item_id', models.CharField(blank=True, max_length=240, null=True, verbose_name='Supplier ERP Item ID')),
                ('sales_order_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Sales Order Number')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Status')),
                ('status_message', models.TextField(blank=True, null=True, verbose_name='Status Message')),
                ('creation_date', models.DateTimeField(blank=True, null=True, verbose_name='Date of Creation')),
                ('created_by', models.CharField(blank=True, max_length=240, null=True, verbose_name='Created By')),
                ('last_update_date', models.DateTimeField(blank=True, null=True, verbose_name='Last Update Date')),
                ('last_updated_by', models.CharField(blank=True, max_length=240, null=True, verbose_name='Last Updated By')),
                ('last_user', models.CharField(blank=True, max_length=240, null=True, verbose_name='Last User')),
                ('network_id', models.CharField(blank=True, max_length=240, null=True, verbose_name='Network ID')),
                ('supplier_id', models.PositiveIntegerField(blank=True, null=True)),
                ('customer_id', models.PositiveIntegerField(blank=True, null=True)),
                ('ship_mode', models.CharField(blank=True, max_length=240, null=True, verbose_name='Shippment Mode')),
                ('order_source', models.CharField(blank=True, max_length=240, null=True, verbose_name='Source of Order')),
            ],
        ),
    ]
