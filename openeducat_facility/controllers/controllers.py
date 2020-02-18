# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatFacility(http.Controller):
#     @http.route('/openeducat_facility/openeducat_facility/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_facility/openeducat_facility/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_facility.listing', {
#             'root': '/openeducat_facility/openeducat_facility',
#             'objects': http.request.env['openeducat_facility.openeducat_facility'].search([]),
#         })

#     @http.route('/openeducat_facility/openeducat_facility/objects/<model("openeducat_facility.openeducat_facility"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_facility.object', {
#             'object': obj
#         })