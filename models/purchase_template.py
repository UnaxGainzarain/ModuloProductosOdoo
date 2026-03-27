from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _tara_status = fields.Selection(
        selection=[
            ('sin_tara', 'Sin tara'),
            ('con_tara', 'Con tara')
        ],
        string='Estado de la Tara',
        default='sin_tara',
        help='Indica si el producto está en perfecto estado o tiene algún defecto físico.'
    )

    purchase_orders= fields.Char(
        string='Pedidos de Compra',
        help='Pedidos de compra asociados al producto.'
    )

    _generic_name = fields.Char(    
        string='Nombre Genérico',
        help='Nombre alternativo para presupuestos con nombres genéricos (ej: Silla de comedor).'
    )