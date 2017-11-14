# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import calendar
from odoo import api, fields, models, tools


class Instance(models.Model):
    _name = 'myodoo.instance'

    name = fields.Char('Name', required=True)
    description = fields.Text(string='Description')
