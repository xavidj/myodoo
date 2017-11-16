# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import calendar
from odoo import api, fields, models, tools


class Instance(models.Model):
    _name = 'myodoo.instance'

    name = fields.Char('Name', required=True)
    description = fields.Text(string='Description')
    client_id = fields.Many2one('res.partner',
        ondelete='set null', string="Client", index=True)
    ip = fields.Char('IP', required=True)
    version = fields.Selection((('10','10.0'), ('8','8.0'),('11','11.0')),'Version')
    status = fields.Selection((('s', 'Lista'), ('f', 'Apagada'), ('a', 'Arrancando')), 'Status')
    backend_login = fields.Char('Backend login');
    backend_password = fields.Char('Backend password');
    postgres_login = fields.Char('Postgres login');
    postgres_password = fields.Char('Postgres password');
    ssh_login = fields.Char('SSH login');
    ssh_password = fields.Char('SSH password');
