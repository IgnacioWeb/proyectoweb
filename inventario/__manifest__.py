# -*- coding: utf-8 -*-
{
    'name': "inventario",

    'summary': """
        asgd sgsd sdgs gds ds gs dgsgsdg gsdgs g sdg""",

    'description': """
        Long description of module's purpose
    """,

    'author': "UTAL",
    'website': "http://www.utalca.cl",

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
        'views/view_stock.xml',
        #'views/templates.xml',
    ],
    
}