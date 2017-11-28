# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, tools
from github import Github
import re



class Sdi_Project_Repositories(models.Model):
    _name = 'sdi_project.sdi_project_repositories'

    name = fields.Char('Name', required=True)
    url = fields.Char('Url', required=True)
    branch_id=fields.Many2one('sdi_project.sdi_project_branches',
        ondelete='set null', string="Branch", index=True)


    @api.multi
    def get_models(self):
        # First create a Github instance:
        settings_obj = self.env['sdi_project.sdi_project_settings']
        module_id = settings_obj.search([], limit=1)
        g = Github(module_id.name, module_id.passw)

        results = re.search('https?:\/\/(?:www\.)?github\.com\/(.+)\/([^\.]+)', self.url)
        if not results:
            raise Exception("Invalid repository url")

        user_login = results.group(1)

        user_repo = results.group(2)

        modules_obj = self.env['sdi_project.sdi_project_models']
        modulesInfo = {}
        # Then play with your Github objects:
        for repo in g.get_organization(user_login).get_repos(self.url):
            if repo.name == user_repo:
                file_contents = repo.get_contents('.',self.branch_id.name)
                for file in file_contents:
                    if file.type=='dir':
                        modulesInfo[file.path]=file.path

        for module in modulesInfo:
            record_data = {
                'name': modulesInfo[module],
            }

            module_id = modules_obj.search([('repositorie_id', '=', self.id),
                                            ('name', '=', modulesInfo[module])], limit=1)
            if not module_id:
                record_data.update({
                    'repositorie_id': self.id
                })
                modules_obj.create(record_data)
            else:
                module_id.write(record_data)
