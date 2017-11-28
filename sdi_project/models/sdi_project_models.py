# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import calendar
from odoo import api, fields, models, tools


class Sdi_Project_Models(models.Model):
    _name = 'sdi_project.sdi_project_models'

    name = fields.Char('Name', required=True)
    repositorie_id=fields.Many2one('sdi_project.sdi_project_repositories',
        ondelete='set null', string="Repository", index=True)
