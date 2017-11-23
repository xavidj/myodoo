# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Partner(models.Model):

    _inherit = 'res.partner'

    instances_count = fields.Integer("Instances", compute='_compute_instances_count')


    @api.multi
    def _compute_instances_count(self):
        instance_data = self.env['myodoo.instance'].read_group([('client_id', 'in', self.ids)], ['client_id'], ['client_id'])
        mapped_data = {act['client_id'][0]: act['client_id_count'] for act in instance_data}
        for partner in self:
            partner.instances_count = mapped_data.get(partner.id, 0)


