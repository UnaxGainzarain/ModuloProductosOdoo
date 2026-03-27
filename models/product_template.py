from odoo import models, fields

class ProductCustomImage(models.Model):
    _name = 'custom_stock.product_image'
    _description = 'Imagen de Producto Personalizada'

    name = fields.Char(string='Descripción', required=True)
    custom_image = fields.Binary(string='Imagen', required=True)
    product_tmpl_id = fields.Many2one('product.template', string='Producto', ondelete='cascade')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_image_ids = fields.One2many(
        'custom_stock.product_image',
        'product_tmpl_id',
        string='Imágenes Adicionales'
    )

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