from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    larosa_featured = fields.Boolean(
        'Feature on La Rosa homepage', copy=False,
        help='Optional priority. Published saleable products appear automatically; this moves a product to the front.')
