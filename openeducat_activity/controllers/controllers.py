# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatActivity(http.Controller):
#     @http.route('/openeducat_activity/openeducat_activity/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_activity/openeducat_activity/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_activity.listing', {
#             'root': '/openeducat_activity/openeducat_activity',
#             'objects': http.request.env['openeducat_activity.openeducat_activity'].search([]),
#         })

#     @http.route('/openeducat_activity/openeducat_activity/objects/<model("openeducat_activity.openeducat_activity"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_activity.object', {
#             'object': obj
#         })