from odoo import api,models,fields


        
        

class champ(models.Model):
    _inherit='account.invoice.line'
    ptaxee=fields.Float('Prix taxe')
    price_unit=fields.Float(compute='_get_price_hors_taxe')
    @api.one
    def _get_price_hors_taxe(self):
        self.price_unit= ((((self.ptaxee -21.24)/1.8)-4.237)/1.01)