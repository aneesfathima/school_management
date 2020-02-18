# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatExam(http.Controller):
#     @http.route('/openeducat_exam/openeducat_exam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_exam/openeducat_exam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_exam.listing', {
#             'root': '/openeducat_exam/openeducat_exam',
#             'objects': http.request.env['openeducat_exam.openeducat_exam'].search([]),
#         })

#     @http.route('/openeducat_exam/openeducat_exam/objects/<model("openeducat_exam.openeducat_exam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_exam.object', {
#             'object': obj
#         })