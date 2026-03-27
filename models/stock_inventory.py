from odoo import models, fields

class StockInventory(models.Model):
    _name = 'custom_stock.inventory'
    _description = 'Stock Inventory'

    name = fields.Char(string='Inventory Reference', required=True)
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    location_id = fields.Many2one('custom_stock.location', string='Location', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='Status', default='draft')
