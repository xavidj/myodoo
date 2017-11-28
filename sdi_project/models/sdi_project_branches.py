# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import calendar
from odoo import api, fields, models, tools


class Sdi_Project_Branches(models.Model):
    _name = 'sdi_project.sdi_project_branches'

    name = fields.Char('Name', required=True)
    description = fields.Char('Description')
