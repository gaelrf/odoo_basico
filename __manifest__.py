# -*- coding: utf-8 -*-
{
    'name': "odoo_basico",

    'summary': """
        proxect basico""",

    'description': """
        Long description of module's purpose
    """,

    'author': "eu",
    'website': "http://www.edu.xunta.gal/iesteis",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/informacion.xml',
        'views/suceso.xml',
        'views/menu.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
