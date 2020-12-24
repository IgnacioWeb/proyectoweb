# -*- coding: utf-8 -*-

from odoo import models, fields, api



class categoriaplatos(models.Model):
    _name = 'inventario.categoria_platos'
    name = fields.Char(string="Categoria",required=True)
    plato_id= fields.One2many(
    'inventario.platos',
    'categoria_platos_id',
    string="Platos"
    )

    total_platos= fields.Integer(
        string="Total platos",compute="_total_platos")

    @api.one
    def _total_platos(self):
        self.total_platos=len(self.plato_id)


class Platos(models.Model):
    _name = 'inventario.platos'

    name = fields.Char(string="Nombre",required=True)
    descripcion= fields.Char(string="Descripcion",required=True)
    cost= fields.Float(string="Valor")
    
    categoria_platos_id= fields.Many2one('inventario.categoria_platos',string="Categoria")