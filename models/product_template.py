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

    _tara_description = fields.Text(
        string='Descripción de la Tara',
        help='Texto libre para describir el defecto (ej: Arañazo de 5cm en pata trasera izquierda).'
    )

    _generic_name = fields.Char(
        string='Nombre Genérico',
        help='Nombre alternativo para presupuestos con nombres genéricos (ej: Silla de comedor).'
    )