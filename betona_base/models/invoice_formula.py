from odoo import fields,api,models

class manufacturing(models.Model):
    _inherit="mrp.production"
    
    def calculer_cout(self):
        
        price=0
        for composant in self.move_raw_ids:
            price+=composant.product_id.standard_price*composant.product_uom_qty
        self.cout=price           
    
    
    cout=fields.Float("cout de la fabrication",compute='calculer_cout')
    
            