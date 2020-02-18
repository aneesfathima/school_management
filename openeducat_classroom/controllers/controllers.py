# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatClassroom(http.Controller):
#     @http.route('/openeducat_classroom/openeducat_classroom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_classroom/openeducat_classroom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_classroom.listing', {
#             'root': '/openeducat_classroom/openeducat_classroom',
#             'objects': http.request.env['openeducat_classroom.openeducat_classroom'].search([]),
#         })

#     @http.route('/openeducat_classroom/openeducat_classroom/objects/<model("openeducat_classroom.openeducat_classroom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_classroom.object', {
#             'object': obj
#         })