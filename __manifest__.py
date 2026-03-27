{
    'name': 'Custom Stock Management',
    'version': '1.0',
    'summary': 'Basic stock management module for Odoo 18',
    'description': 'Manage stock locations and inventory records.',
    'category': 'Inventory',
    'author': 'Unax',
    'depends': ['base', 'product', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_location_views.xml',
        'views/stock_inventory_views.xml',
        'views/product_template_views.xml',
        'views/purchase_template_views.xml',
    ],
    'installable': True,
    'application': True,
}
