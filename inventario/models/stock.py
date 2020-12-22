# -*- coding: utf-8 -*-

from odoo import models, fields, api

class categoriaproductos(models.Model):
    _name = 'inventario.categoria_productos'
    name = fields.Char(string="Caegoria",required=True)
    producto_id= fields.One2many(
    'inventario.stock',
    'categoria_productos_id',
    string="Productos"
    )

    total_productos= fields.Integer(
        string="Total productos",compute="_total_productos")

    @api.one
    def _total_productos(self):
        self.total_productos=len(self.producto_id)

class Stock(models.Model):
    _name = 'inventario.stock'

    name = fields.Char(string="Nombre",required=True)
    cantidad= fields.Integer(string="Stock",required=True)
    cost= fields.Float(string="Valor unitario")

    date= fields.Date("Fecha ingreso")

    categoria_productos_id= fields.Many2one('inventario.categoria_productos',string="Categoria")
