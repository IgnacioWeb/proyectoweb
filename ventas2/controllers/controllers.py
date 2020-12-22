# -*- coding: utf-8 -*-
from odoo import http

# class Ventas2(http.Controller):
#     @http.route('/ventas2/ventas2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ventas2/ventas2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ventas2.listing', {
#             'root': '/ventas2/ventas2',
#             'objects': http.request.env['ventas2.ventas2'].search([]),
#         })

#     @http.route('/ventas2/ventas2/objects/<model("ventas2.ventas2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ventas2.object', {
#             'object': obj
#         })