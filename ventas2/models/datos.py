# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tipodato(models.Model):
    _name = 'ventas2.datos2'

    name = fields.Char(string="Nombre", required=True)
    dato_ids = fields.One2many(
        'ventas2.datos',
        'tipo_datos_id',
        string='Datos')

    total_datos = fields.Integer(String="Total de datos", compute="_total_datos")

    @api.one
    def _total_datos(self):
        self.total_datos = len(self.dato_ids)

class Datos(models.Model):
    _name = 'ventas2.datos'

    name = fields.Char(string="Nombre", required=True)
    cost = fields.Float(string="Precio", required=True)
    date = fields.Date(string="Fecha de compra", required=True)

    tipo_datos_id = fields.Many2one('ventas2.datos2', string="Tipo de Alimento")
