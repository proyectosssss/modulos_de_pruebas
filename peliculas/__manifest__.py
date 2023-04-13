# -*- coding:utf-8 -*-

{
    'name': 'Modulo de peliculas',
    'version': '1.0',
    'depends': [
        'contacts',
        'mail',
    ],
    'author': 'Eduardo Velaochaga',
    'category': 'Peliculas',
    'website': 'http://www.google.com',
    'summary': 'Modulo de presupuestos para peliculas',
    'description': '''
    Modulo para hacer presupuestos de peliculas
    ''',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/categoria.xml',
        'data/secuencia.xml',
        'wizard/update_wizard_views.xml',
        'report/reporte_pelicula.xml',
        'views/presupuesto_views.xml',
        'views/menu.xml',
    ],
}