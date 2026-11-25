{
    'name': 'La Rosa — Website & Shop',
    'version': '19.0.1.0.0',
    'summary': 'Arts, crafts and stationery storefront with native Odoo eCommerce and La Rosa backend colours',
    'category': 'Website/eCommerce',
    'author': 'Spxcorp Limited',
    'website': 'https://spxcorp.net',
    'license': 'LGPL-3',
    'depends': ['website_sale'],
    'data': [
        'views/settings.xml', 'views/layout.xml', 'views/commerce.xml',
        'data/categories.xml', 'data/pages.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'larosa_website/static/src/css/brand_variables.scss'),
        ],
        'web.assets_frontend': [
            'larosa_website/static/src/css/fonts.css',
            'larosa_website/static/src/css/storefront.scss',
            'larosa_website/static/src/js/storefront.js',
        ],
        'web.assets_backend': ['larosa_website/static/src/css/backend.scss'],
    },
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
}
