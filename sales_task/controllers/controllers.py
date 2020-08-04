# -*- coding: utf-8 -*-
# from odoo import http


# class SalesTask(http.Controller):
#     @http.route('/sales_task/sales_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_task/sales_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_task.listing', {
#             'root': '/sales_task/sales_task',
#             'objects': http.request.env['sales_task.sales_task'].search([]),
#         })

#     @http.route('/sales_task/sales_task/objects/<model("sales_task.sales_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_task.object', {
#             'object': obj
#         })
