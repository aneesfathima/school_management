# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatAssignment(http.Controller):
#     @http.route('/openeducat_assignment/openeducat_assignment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_assignment/openeducat_assignment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_assignment.listing', {
#             'root': '/openeducat_assignment/openeducat_assignment',
#             'objects': http.request.env['openeducat_assignment.openeducat_assignment'].search([]),
#         })

#     @http.route('/openeducat_assignment/openeducat_assignment/objects/<model("openeducat_assignment.openeducat_assignment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_assignment.object', {
#             'object': obj
#         })