# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatFees(http.Controller):
#     @http.route('/openeducat_fees/openeducat_fees/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_fees/openeducat_fees/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_fees.listing', {
#             'root': '/openeducat_fees/openeducat_fees',
#             'objects': http.request.env['openeducat_fees.openeducat_fees'].search([]),
#         })

#     @http.route('/openeducat_fees/openeducat_fees/objects/<model("openeducat_fees.openeducat_fees"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_fees.object', {
#             'object': obj
#         })