#-*- coding: utf-8 -*-
from odoo import api,fields,models
from datetime import date


class livraison(models.Model):
    _inherit='stock.picking'
    
    res=fields.Text('Réservé à la direction')
    chauff=fields.Char('Chauffeur')
    cam=fields.Char('Camion')
    ouv=fields.Char('Ouvrage')
#     pomp=fields.Selection([('oui', 'Oui'), ('non', 'Non')], string='Pompage')
    adresse=fields.Char('Adresse du chantier')
    reference=fields.Char('Référence')
    pomp=fields.Boolean('Pompage')
    npomp=fields.Boolean('Sans Pompage')
    dc=fields.Char('Départ central')
    ac=fields.Char('Arrivée client')
    gravier=fields.Selection([('dj','Dj oust'),('Dj','Dj Ressas')])
    adju=fields.Char('Adjuvant')
    typ1=fields.Boolean('5/8')
    typ2=fields.Boolean('8/12')
    typ3=fields.Boolean('12/20')
    typ4=fields.Boolean('4/15')
    dosage1=fields.Boolean('CPI 42.5')
    dosage2=fields.Boolean('HRS')
    type1=fields.Boolean('250')
    type2=fields.Boolean('300')
    type3=fields.Boolean('350')
    type4=fields.Boolean('400')
    sab=fields.Boolean('sable')
    eau=fields.Boolean('Eau')
    nb=fields.Integer('Nombre')
    cl=fields.Char('client')
    rp=fields.Char('Représantant')
    mr=fields.Char('Monsieur')
    qr=fields.Float('Quantité de beton reçue')
    qa=fields.Float('Quantité d''eau ajoutée')
    date_de_livraison=fields.Date("date de livraison")
    