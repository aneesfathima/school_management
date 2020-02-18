# -*- coding: utf-8 -*-
from odoo import http

# class OpeneducatTimetable(http.Controller):
#     @http.route('/openeducat_timetable/openeducat_timetable/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_timetable/openeducat_timetable/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_timetable.listing', {
#             'root': '/openeducat_timetable/openeducat_timetable',
#             'objects': http.request.env['openeducat_timetable.openeducat_timetable'].search([]),
#         })

#     @http.route('/openeducat_timetable/openeducat_timetable/objects/<model("openeducat_timetable.openeducat_timetable"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_timetable.object', {
#             'object': obj
#         })