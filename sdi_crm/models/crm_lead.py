# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    type_id = fields.Many2one('sdi_crm.sdi_project_type', 'Type', index=True)

    @api.multi
    def action_set_won(self):
        super(CrmLead, self).action_set_won()
        for lead in self:
            if lead.type_id.type== 'odoo':
                project_obj = self.env['project.project']
                record_data = {
                    'name': lead.name,
                    'type_id':lead.type_id.id,
                    'partner_id': lead.partner_id.id,
                }
                project_obj.create(record_data)
        return True

