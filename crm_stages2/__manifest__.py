# -*- coding:utf-8 -*-

{
    'name': 'Stages CRM',
    'depends': ['base',
                'crm',
                ],
    'data':['views/views.xml',
            'views/actions.xml',
            'views/data.xml',
            'security/securityxml.xml',
            'security/ir.model.access.csv',
            ],
    'description':"""

    THIS MODULE ADD A FIELD ON WEBSITE.TRACK MODEL AND A METHOD TO FETCH IDS FROM URL.
    
    """
}