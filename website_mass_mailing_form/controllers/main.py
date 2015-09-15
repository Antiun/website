# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import http


class website_mass_mailing_form(http.Controller):

    @http.route(['/website/mass_mailing/signup/<slug>'], type='http',
                auth="public", website=True)
    def mailing_list_signup(self, slug, **post):
        cr, uid, context = request.cr, request.uid, request.context
        mailing_list_obj = request.registry['mail.mass_mailing.list']
        list_id = mailing_list_obj.search(
            cr, uid, [('form_slug', '=', slug),
                      ('website_published', '=', True)], context=context)
        if not list_id:
            return request.redirect('/')
        mailing_list = mailing_list_obj.browse(cr, uid, list_id,
                                               context=context)
        values = {
            'description': mailing_list.form_description,
            'list_id': list_id
        }
        return request.website.render(
            "website_mass_mailing_form.mailing_list_signup", values)

    @http.route(['/website/mass_mailing/signup/success'], type='http',
                auth="public", website=True)
    def mailing_list_signup_success(self, **post):
        list_id = post.get('list_id', False)
        if not list_id:
            return request.redirect('/')
        cr, uid, context = request.cr, request.uid, request.context
        mailing_list_obj = request.registry['mail.mass_mailing.list']
        mailing_list = mailing_list_obj.browse(cr, uid, list_id,
                                               context=context)
        if not mailing_list or not mailing_list.website_published:
            return request.redirect('/')
        mailing_list.website_signup(post.get('email'), post.get('name'))
        values = {'message': mailing_list.signup_message}
        return request.website.render(
            'website_mass_mailing_form.mailing_list_signup_success', values)
