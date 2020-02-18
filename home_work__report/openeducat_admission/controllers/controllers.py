# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatAdmission(http.Controller):
#     @http.route('/openeducat_admission/openeducat_admission/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_admission/openeducat_admission/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_admission.listing', {
#             'root': '/openeducat_admission/openeducat_admission',
#             'objects': http.request.env['openeducat_admission.openeducat_admission'].search([]),
#         })

#     @http.route('/openeducat_admission/openeducat_admission/objects/<model("openeducat_admission.openeducat_admission"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_admission.object', {
#             'object': obj
#         })