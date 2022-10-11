# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class hrUpdate(models.Model):
    _inherit = 'hr.employee'
     
    num_imat = fields.Char(string='Numéro immatriculation CNSS')
    salaire = fields.Char(string='Salaire')
    salaire_decl = fields.Char(string='Salaire déclarer')

        
