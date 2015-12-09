# -*- coding: utf-8 -*-
# © 2015 Antiun Ingenieria S.L. - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Website dynamic Google Map",
    'summary': "Show dynamic Google map in 'Contact us' page",
    'category': 'Website',
    'version': '8.0.1.0.0',
    'depends': [
        'website',
        'base_geolocalize_map',
    ],
    'data': [
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/website_templates.xml',
    ],
    'author': 'Antiun Ingeniería S.L., '
              'Odoo Community Association (OCA)',
    'website': 'http://www.antiun.com',
    'license': 'AGPL-3',
    'installable': True,
}
