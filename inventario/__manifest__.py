# -*- coding: utf-8 -*-
{
    'name': "inventario",

    'summary': """
    El módulo de inventario tiene como finalidad administrar y gestionar las distintas existencias que dispone una organización, en donde el usuario podrá agregar, modificar, eliminar o realizar solicitudes de pedidos, permitiendo de esta manera abaratar costes por excesos o escasez en los productos almacenados, además ayuda a determinar cuántas unidades son necesarias para ordenar o producir, en qué momento deberán ordenarse, al igual que coordinar las funciones con otras áreas como compras y ventas.
        """,

    'description': """
        El módulo de inventario tiene como finalidad administrar y gestionar las distintas existencias que dispone una organización, en donde el usuario podrá agregar, modificar, eliminar o realizar solicitudes de pedidos, permitiendo de esta manera abaratar costes por excesos o escasez en los productos almacenados, además ayuda a determinar cuántas unidades son necesarias para ordenar o producir, en qué momento deberán ordenarse, al igual que coordinar las funciones con otras áreas como compras y ventas.
    """,

    'author': "Francisco Delzon",
    'website': "",

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