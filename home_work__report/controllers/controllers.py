# -*- coding: utf-8 -*-
from odoo import http

# class HomeWorkReport(http.Controller):
#     @http.route('/home_work__report/home_work__report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/home_work__report/home_work__report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('home_work__report.listing', {
#             'root': '/home_work__report/home_work__report',
#             'objects': http.request.env['home_work__report.home_work__report'].search([]),
#         })

#     @http.route('/home_work__report/home_work__report/objects/<model("home_work__report.home_work__report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('home_work__report.object', {
#             'object': obj
#         })