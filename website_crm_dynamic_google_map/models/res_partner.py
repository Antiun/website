# -*- coding: utf-8 -*-
# © 2015 Antiun Ingenieria S.L. - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
from openerp.addons.website.models.website import urlplus
from openerp.tools.float_utils import float_is_zero


class ResPartner(models.Model):
    _inherit = 'res.partner'

    google_map_type = fields.Selection(
        [('static', 'Static map'),
         ('dynamic', 'Dynamic map')],
        string="GoogleMap type", default='static')

    @api.multi
    def google_map_img(self, zoom=8, width=298, height=298):
        super(ResPartner, self).google_map_img(
            zoom=zoom, width=width, height=height)
        self.ensure_one()
        lat = self.partner_latitude
        lon = self.partner_longitude
        if (not float_is_zero(lat, precision_digits=8) and
                not float_is_zero(lon, precision_digits=8)):
            position = '%3.8f, %3.8f' % (lat, lon)
        else:
            position = '%s, %s %s, %s' % (
                self.street or '',
                self.city or '',
                self.zip or '',
                self.country_id and
                self.country_id.name_get()[0][1] or ''),

        if self.google_map_type == 'static':
            params = {
                'center': position,
                'size': "%sx%s" % (height, width),
                'zoom': zoom,
                'sensor': 'false',
            }
            if self.google_map_marker:
                params['markers'] = params['center']
            url_base = '//maps.googleapis.com/maps/api/staticmap'
        else:
            params = {
                'q': '%s %s' % (self.name, position),
                'ie': 'UTF8',
                'output': 'embed',
                'z': zoom,
            }
            url_base = '//maps.google.com/maps'
        return urlplus(url_base, params)
