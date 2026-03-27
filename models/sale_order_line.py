from odoo import api, fields, models, _

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    use_existing_stock = fields.Boolean(
        string='Usar Stock Existente',
        help='Si está marcado, se priorizará el envío desde el stock físico disponible en el almacén.',
        default=False
    )

    @api.onchange('product_id')
    def _onchange_product_stock_warning(self):
        if not self.product_id:
            return
            
        # Comprobar si hay stock físico real (qty_available)
        if hasattr(self.product_id, 'qty_available') and self.product_id.qty_available > 0:
            return {
                'warning': {
                    'title': "Stock Disponible Localizado",
                    'message': "Este producto tiene %s unidades actualmente en el almacén.\nPor favor, marca la casilla 'Usar Stock Existente' en la línea si decides utilizar este stock para evitar pedir más al proveedor." % self.product_id.qty_available
                }
            }
