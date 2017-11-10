# -*- coding: utf-8 -*-
# Copyright 2016 Antonio Espinosa <antonio.espinosa@tecnativa.com>
# Copyright 2012-2017 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import calendar
from odoo import api, fields, models, tools


class People(models.Model):
    _name = 'myodoo.people'

    age = fields.Integer(string='Age')
    name = fields.Char('Name', required=True)
    avatar = fields.Binary(string='Avatar')
