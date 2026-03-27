{
    'name': 'Custom Stock Management',
    'version': '1.0',
    'summary': 'Basic stock management module for Odoo 18',
    'description': 'Manage stock locations and inventory records.',
    'category': 'Inventory',
    'author': 'Unax',
    'depends': ['base', 'product', 'purchase', 'stock', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/purchase_template_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
}
