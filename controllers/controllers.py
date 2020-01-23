# -*- coding: utf-8 -*-
from odoo import http

# class VitUudpMenuHiddenV2(http.Controller):
#     @http.route('/vit_uudp_menu_hidden_v2/vit_uudp_menu_hidden_v2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_uudp_menu_hidden_v2/vit_uudp_menu_hidden_v2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_uudp_menu_hidden_v2.listing', {
#             'root': '/vit_uudp_menu_hidden_v2/vit_uudp_menu_hidden_v2',
#             'objects': http.request.env['vit_uudp_menu_hidden_v2.vit_uudp_menu_hidden_v2'].search([]),
#         })

#     @http.route('/vit_uudp_menu_hidden_v2/vit_uudp_menu_hidden_v2/objects/<model("vit_uudp_menu_hidden_v2.vit_uudp_menu_hidden_v2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_uudp_menu_hidden_v2.object', {
#             'object': obj
#         })