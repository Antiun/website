# -*- coding: utf-8 -*-
# © 2015 Antiun Ingenieria S.L. - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    map_marker = fields.Boolean(
        string="Show marker on map", related='partner_id.map_marker')
    map_zoom = fields.Integer(
        string="Map zoom", related='partner_id.map_zoom')
    partner_latitude = fields.Float(
        string="Geo Latitude", digits=(16, 5),
        related='partner_id.partner_latitude')
    partner_longitude = fields.Float(
        string="Geo Longitude", digits=(16, 5),
        related='partner_id.partner_longitude')
    date_localization = fields.Date(
        string="Geo Localization Date", related='partner_id.date_localization')

    @api.multi
    def geo_localize(self):
        for company in self:
            company.partner_id.geo_localize()
        return True
