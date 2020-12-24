
from odoo import models, fields, api

class RegTrans(models.Model):
    _name = 'ventas2.trans'

    name = fields.Char(string="Nombre", required=True)
    trans_ids = fields.One2many(
        'ventas2.trans2',
        'tipo_trans2_id',
        string='Datos')

    total_trans2 = fields.Integer(String="Total de datos", compute="_total_trans2")

    @api.one
    def _total_trans2(self):
        self.total_trans2 = len(self.trans_ids)

class Transaccion(models.Model):
    _name = 'ventas2.trans2'

    name = fields.Char(string="Nombre", required=True)
    cost = fields.Float(string="Precio", required=True)
    date = fields.Date(string="Fecha de compra", required=True)

    tipo_trans2_id = fields.Many2one('ventas2.trans', string="Tipo de Transaccion")