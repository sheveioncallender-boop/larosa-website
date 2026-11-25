from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    larosa_brand_enabled = fields.Boolean(related='website_id.larosa_brand_enabled', readonly=False)
    larosa_phone = fields.Char(related='website_id.larosa_phone', readonly=False)
    larosa_address = fields.Text(related='website_id.larosa_address', readonly=False)
    larosa_hours = fields.Text(related='website_id.larosa_hours', readonly=False)
    larosa_whatsapp = fields.Char(related='website_id.larosa_whatsapp', readonly=False)
