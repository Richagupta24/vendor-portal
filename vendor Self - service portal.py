from dataclasses import fields
from django.db import models

from django.db.models.base import Model


class VendorForecast (Model):
    _name = 'vendor.forecast'

    product_id = fields.Many2one('product.product', string='Product')
    expected_quantity = fields.Integer(string='Expected Quantity')
    forecast_date = fields.Date(string='Forecast Date')
class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request' 
    order_id = fields.Many2one('sale.order', string='Order')
    adjustment_detail = fields.Text(string='Adjustment Detail')
    comment = fields.Text(string='Comment')
    class VendorForecast(models.Model):
     

     class Vendor(models.Model):
      name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # Add more fields as needed

    # ...

    def action_download_report(self):
        # Generate report using Odoo's reporting capabilities or external libraries
        pass
    class VendorAdjustmentRequestWizard(models.TransientModel):_name = 'vendor.adjustment.request.wizard'

    # ...

    def submit_adjustment_request(self):
        # Submit the adjustment request
        pass