# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ped(models.Model):
    _name = 'pedido.compra'

    name= fields.Char(string="Detalle", required =True)

    pedido_id = fields.one2many('detalle.compra','detalle_compra_id', compute="_info_compra")

    @api.one
    def _info_compra(self):
        self.pedido_id =len(self.pedido_id)


class com(models.Model):
    _name = 'detalle.compra'

    name = fields.Char(string="Nombre", requiered=True)

    quantity = fields.Integer(string="Cantidad", requiered=True)

    info = fields.Char(string="Detalle")

    purchase_date = fields.Date("Fecha de compra")

    detalle_compra_id = fields.Many2one('pedido.compra', string="Detalle Compra")