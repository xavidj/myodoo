# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import calendar
from odoo import api, fields, models, tools


class Sdi_Project_Type(models.Model):
    _name = 'sdi_crm.sdi_project_type'

    name = fields.Char('Name', required=True)
    type = fields.Selection((('odoo', 'odoo'), ('a3', 'a3'), ('sdi', 'sdi'), ('other', 'other')), 'Type', required=True)
    description = fields.Text(string='Description')
