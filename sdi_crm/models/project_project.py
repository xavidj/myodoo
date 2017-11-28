# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProjectProject(models.Model):

    _inherit = 'project.project'

    type_id = fields.Many2one('sdi_crm.sdi_project_type', 'Type', index=True)





