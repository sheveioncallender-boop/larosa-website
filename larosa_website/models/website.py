from urllib.parse import urlencode
from odoo import fields, models
from odoo.fields import Domain


class Website(models.Model):
    _inherit = 'website'

    larosa_brand_enabled = fields.Boolean('La Rosa storefront', default=False)
    larosa_phone = fields.Char('Store telephone')
    larosa_address = fields.Text('Store address')
    larosa_hours = fields.Text('Opening hours', translate=True)
    larosa_whatsapp = fields.Char('WhatsApp number', help='Full international number, e.g. 18684634578.')

    def _larosa_phone_url(self):
        self.ensure_one()
        return 'tel:' + ''.join(c for c in (self.larosa_phone or '') if c.isdigit() or c == '+')

    def _larosa_whatsapp_url(self):
        self.ensure_one()
        number = ''.join(c for c in (self.larosa_whatsapp or '') if c.isdigit())
        return 'https://wa.me/' + number if number else False

    def _larosa_directions_url(self):
        self.ensure_one()
        return 'https://www.google.com/maps/dir/?' + urlencode({
            'api': '1', 'destination': (self.larosa_address or 'North Hills Plaza, Santa Cruz, Trinidad and Tobago').replace('\n', ', '),
        })

    def _larosa_map_url(self):
        self.ensure_one()
        return 'https://maps.google.com/maps?' + urlencode({
            'q': (self.larosa_address or 'North Hills Plaza, Santa Cruz, Trinidad and Tobago').replace('\n', ', '),
            'output': 'embed',
        })

    def _larosa_products(self):
        self.ensure_one()
        Product = self.env['product.template'].with_context(website_id=self.id)
        if not self.larosa_brand_enabled or not self.has_ecommerce_access():
            return Product.browse()
        # Match native shop/company/website rules; never elevate catalogue access.
        return Product.search(Domain.AND([
            self.sale_product_domain(),
            [('active', '=', True), ('is_published', '=', True)],
        ]), order='larosa_featured desc, website_sequence, id desc', limit=8)

    def _larosa_categories(self):
        self.ensure_one()
        Category = self.env['product.public.category'].with_context(website_id=self.id)
        if not self.larosa_brand_enabled or not self.has_ecommerce_access():
            return Category.browse()
        return Category.search(Domain.AND([
            self.website_domain(), [('has_published_products', '=', True)],
        ]), order='sequence, name, id', limit=8)

    def _larosa_category_url(self, xmlid):
        self.ensure_one()
        category = self.env.ref('larosa_website.' + xmlid, raise_if_not_found=False)
        if category:
            # Public record rules hide empty categories. Search before reading fields.
            category = self.env['product.public.category'].with_context(website_id=self.id).search(
                Domain.AND([self.website_domain(), [('id', '=', category.id)]]), limit=1)
        if category:
            return '/shop/category/' + self.env['ir.http']._slug(category)
        return '/shop'
