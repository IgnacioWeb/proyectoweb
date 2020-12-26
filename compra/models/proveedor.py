# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tipoprov(models.Model):
     _name = 'tipo.provedor'

     info = fields.Char(string="Descripción Proveedor", requiered=True)

     proveedor_id = fields.one2Many('proveedor.compra','info_proveedor_id', string = "Info")

     info_prov = fields.Char(String="Info Proveedor", compute="_info_prov")
    
     @api.one
     def _info_prov(self):
         self.info_prov = len(self.info_prov)


class prov(models.Model):
    _name = 'proveedor.compra'

    name = fields.Char(string="Nombre", requiered=True)

    phone= fields.Integer(string="Teléfono", requiered=True)

    adress = fields.Char(string="Dirección")

    email = fields.Char(string="Email", requered=True)
     
    info_prov_id =fields.Many2one('proveedor.compra', string = "Info")

