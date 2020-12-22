# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TipoDato(models.Model):
    _name = 'ventas2.datos2'

    name = fields.Char(string="Nombre", required=True)
