# -*- coding: utf-8 -*-
{
    'name': "ACH Inventory Report",
    'summary': """
        Inventory Report""",
    'description': """
        Inventory Report
    """,
    'author': "Gt Alchemy Development",
    'license': 'LGPL-3',
    'support': 'developmentalchemygx@gmail.com',
    'category': 'Stock',
    'version': '1.1',   
    'depends': ['base', 
                'stock',
                'report_xlsx',],
    'data': [
        'security/ir.model.access.csv',
        'reports/inventory_report_xlsx.xml',
        'wizard/inventory_report.xml',
    ],
    'images': ['static/description/banner.png'],
}