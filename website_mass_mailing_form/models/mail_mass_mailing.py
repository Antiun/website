# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import models, fields, _


class MailMassMailing(models.Model):
    _name = 'mail.mass_mailing.list'
    _inherit = ['mail.mass_mailing.list', 'mail.thread']

    form_slug = fields.Char(string='Form slug')
    website_published = fields.Boolean(string='Publish',
                                       help="Publish on the website")
    form_description = fields.Html(string='Form description')
    signup_message = fields.Html(string='Sign up message')
    unsubscribe_message = fields.Html(string='Unsubscribe message')
    signup_template = fields.Many2one(comodel_name='email.template')
    unsubscribe_template = fields.Many2one(comodel_name='email.template')

    _sql_constraints = [
        ('form_slug_uniq', 'unique(form_slug)', _('Form slug must be unique.'))
    ]

    def website_signup(self, email, name):
        contact_obj = self.env['mail.mass_mailing.contact']
        contact = contact_obj.search([('email', '=', email),
                                      ('list_id', '=', self.id)])
        if contact:
            if contact.opt_out:
                contact.opt_out = False
                return True
            return False
        contact_obj.create({'email': email, 'name': name, 'list_id': self.id})
        return True
