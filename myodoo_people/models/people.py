# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import calendar
from odoo import api, fields, models, tools


class People(models.Model):
    _name = 'myodoo.people'

    age = fields.Integer(string='Age')
    name = fields.Char('Name', required=True)
    avatar = fields.Binary(string='Avatar')
    latitud= fields.Float(string="Latitud")
    longitud = fields.Float(string="Longitud")
