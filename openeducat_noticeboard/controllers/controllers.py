# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatNoticeboard(http.Controller):
#     @http.route('/openeducat_noticeboard/openeducat_noticeboard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_noticeboard/openeducat_noticeboard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_noticeboard.listing', {
#             'root': '/openeducat_noticeboard/openeducat_noticeboard',
#             'objects': http.request.env['openeducat_noticeboard.openeducat_noticeboard'].search([]),
#         })

#     @http.route('/openeducat_noticeboard/openeducat_noticeboard/objects/<model("openeducat_noticeboard.openeducat_noticeboard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_noticeboard.object', {
#             'object': obj
#         })