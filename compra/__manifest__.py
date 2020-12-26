# -*- coding: utf-8 -*-
{
    'name': "compra",

    'summary': """
        Gestionar los datos referentes a el proceso de compras de la empresa""",
       
    'description': """
        'encargado de almacenar los datos de compras de insumos y proveedores'
    """,

    'author': "Luis Muñoz",
   

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_proveedor.xml',
        'views/view_pedidos.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}