from odoo import models, fields

class ProductCustomFile(models.Model):
    _name = 'custom_stock.product_file'
    _description = 'Archivo de Producto Personalizado'

    description = fields.Char(string='Descripción del Archivo', required=True)
    product_tmpl_id = fields.Many2one('product.template', string='Producto', ondelete='cascade')
    custom_file = fields.Binary(string='Archivo', required=True)
    file_name = fields.Char(string='Nombre del Archivo')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_file_ids = fields.One2many(
        'custom_stock.product_file', 
        'product_tmpl_id', 
        string='Archivos Adicionales'
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