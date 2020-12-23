
from odoo import models, fields, api

class Transaccion(models.Model):
    _name = 'ventas2.trans' 
    _recname = 'TipoTransaccion'

    TipoTransaccion = fields.Char(string="Tipo de transacción", required=True)
    Descripcion = fields.Char(string="Descripción del movimiento", required=True)