# -*- coding: utf-8 -*-
# © 2015 Antiun Ingenieria S.L. - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    map_marker = fields.Boolean(string='Show marker on map', default=True)
    map_zoom = fields.Integer(string="Map zoom", default=8)
