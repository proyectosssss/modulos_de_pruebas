# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Tema',
    'description': 'Default website theme',
    'category': 'Theme',
    'sequence': 1000,
    'version': '1.0',
    'depends': ['website'],
    'data':['views/header.xml','views/footer.xml','views/homepage.xml','views/custom_page.xml','views/menus.xml','views/snippets/snippet1.xml','views/snippets/snippets.xml'],
    'assets': {
        'web.assets_frontend': [
             'theme_tema/static/src/scss/styles.scss',
             'theme_tema/static/src/scss/style_snippets.scss',
        ],
        'web._assets_primary_variables': [
                'theme_tema/static/src/scss/primary_variables.scss',
            ],
    },
    'images': [
     
    ],
    'snippet_lists': {
        
    },
    'license': 'LGPL-3',
}
