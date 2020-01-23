# -*- coding: utf-8 -*-
{
    'name': "UUDP Menu Hidden 2.0",

    'summary': """
        Menyembunyikan menu pencairan parsial""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Iqbal Abdurrahman",
    'website': "http://www.vitarining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2.0',

    # any module necessary for this one to work correctly
    'depends': [
                'base',
                'vit_uudp',
                ],

    # always loaded
    'data': [
        'security/group.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}