# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import models, fields, api


class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'website.config.settings'

    recaptcha_site_key = fields.Char(
        string='reCaptcha site key',
        related='website_id.recaptcha_site_key',
        store=True
    )

    recaptcha_secret = fields.Char(
        string='reCaptcha secret key',
        related='website_id.recaptcha_secret',
        store=True
    )
