# -*- coding: utf-8 -*-
from odoo import http

# class MethodCrmSoConfirm(http.Controller):
#     @http.route('/method_crm_so_confirm/method_crm_so_confirm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_crm_so_confirm/method_crm_so_confirm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_crm_so_confirm.listing', {
#             'root': '/method_crm_so_confirm/method_crm_so_confirm',
#             'objects': http.request.env['method_crm_so_confirm.method_crm_so_confirm'].search([]),
#         })

#     @http.route('/method_crm_so_confirm/method_crm_so_confirm/objects/<model("method_crm_so_confirm.method_crm_so_confirm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_crm_so_confirm.object', {
#             'object': obj
#         })