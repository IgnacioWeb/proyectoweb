# -*- coding: utf-8 -*-
{
    'name': "ventas2",

    'summary': """
        Proyecto de ventas en WEB2""",

    'description': """
        Sistema que permite administrar acciones de ventas en pequeñas empresas.
    """,

    'author': "Ignacio ",
    'website': "http://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_datos.xml', 
        'views/boleta.xml',
        'views/transacciones.xml',
        'views/ttrans.xml',
        #'views/templates.xml',
    ],
    'application': True, 'instalable': True,
}