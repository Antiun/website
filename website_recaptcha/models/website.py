# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

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
