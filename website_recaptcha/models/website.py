# -*- coding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright :
#        (c) 2015 Antiun Ingenieria, SL (Madrid, Spain, http://www.antiun.com)
#                 Antonio Espinosa <antonioea@antiun.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields
from openerp.tools.translate import _
import requests


class Website(models.Model):
    _inherit = 'website'

    recaptcha_site_key = fields.Char(string='reCaptcha site key')
    recaptcha_secret = fields.Char(string='reCaptcha secret key')

    _recaptcha_last_error = []
    _recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'

    def recaptcha_enabled(self):
        if self.recaptcha_site_key and self.recaptcha_secret:
            return True
        return False

    def recaptcha_verify(self, response):
        post_data = {
            'secret': self.recaptcha_secret,
            'response': response
        }
        self._recaptcha_last_error = []
        request_data = requests.post(
            self._recaptcha_url, data=post_data).json()
        if request_data['success']:
            return True
        self._recaptcha_last_error = request_data['error_codes']
        return False

    def recaptcha_last_error(self):
        if ('missing-input-secret' in self._recaptcha_last_error
                or 'invalid-input-secret' in self._recaptcha_last_error):
            return _('Captcha error. Please, try it later.')
        if 'missing-input-response' in self._recaptcha_last_error:
            return _('Empty captcha. Please, type it.')
        if 'invalid-input-response' in self._recaptcha_last_error:
            return _('Wrong captcha. Please, type it again.')
        return False
