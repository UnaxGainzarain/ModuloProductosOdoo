from odoo import models, fields

class StockLocation(models.Model):
    _name = 'custom_stock.location'
    _description = 'Stock Location'

    name = fields.Char(string='Location Name', required=True)
    code = fields.Char(string='Location Code')
    active = fields.Boolean(default=True)
