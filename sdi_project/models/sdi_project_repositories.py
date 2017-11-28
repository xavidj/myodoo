# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import calendar
from odoo import api, fields, models, tools


class Sdi_Project_Repositories(models.Model):
    _name = 'sdi_project.sdi_project_repositoriese'

    name = fields.Char('Name', required=True)
    url = fields.Char('Url', required=True)
    branch_id=fields.Many2one('sdi_project.sdi_project_branches',
        ondelete='set null', string="Branch", index=True)
