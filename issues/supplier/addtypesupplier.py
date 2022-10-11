# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
#from stdnum.ru.inn import calc_company_check_digit
#from orca.messages import LOCATION_NOT_FOUND_BRIEF
#from reportlab.graphics.renderPM import save
#from test.support import requires_IEEE_754

class addtypesupplier(models.Model):
    _inherit = 'res.partner'
     
    type_supplier = fields.Selection(string='Type fournisseur',
                    selection=[('supplier_a', 'Fournisseur A'), ('supplier_b', 'Fournisseur B')],required=True)
    
class grouptypesupplieraccountpayment(models.Model):
    _inherit = 'account.payment'
     
    type_partner_ap = fields.Selection(string='Type fournisseur',related='partner_id.type_supplier',store=True)
    
class grouptypesupplieraccountmove(models.Model):
    _inherit = 'account.move'
     
    type_partner_am = fields.Selection(string='Type fournisseur',related='partner_id.type_supplier',store=True)
    partner_n = fields.Char(string='Fournisseur',related='partner_id.name',store=True)
    
    
    
class grouptypesupplierpurchaseorder(models.Model):
    _inherit = 'purchase.order'

    type_partner_po = fields.Selection(string='Type fournisseur',related='partner_id.type_supplier',store=True)
        