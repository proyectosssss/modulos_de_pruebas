# -*- coding:utf-8 -*-

{
    'name': 'Custom Web',
    'depends': ['website',
                'web',
                'base',
                ],
    'assets': {
        'web.assets_backend': [
            'custom_web/static/src/jscript.js',
        ],
        'web.assets_frontend': [
            'custom_web/static/src/estilos.css',
        ],
        'web._assets_primary_variables': [
            'custom_web/static/src/scss/customizado.scss',
        ],
    },
    
}