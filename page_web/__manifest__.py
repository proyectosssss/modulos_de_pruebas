# -*- coding:utf-8 -*-

{
    'name': 'Pagina web',
    'depends': ['web',
                'website',
                'base',
                ],
    'data':['views/homepage.xml',
            'views/extra_pages.xml',
            ],
    'assets': {
        'web.assets_frontend': [
            'page_web/static/src/estilo.css',
            'page_web/static/src/js/hoja.js',
        ],  
    },
    
}