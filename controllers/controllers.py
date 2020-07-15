# -*- coding: utf-8 -*-
# from odoo import http


# class TechPurchase(http.Controller):
#     @http.route('/tech_purchase/tech_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_purchase/tech_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_purchase.listing', {
#             'root': '/tech_purchase/tech_purchase',
#             'objects': http.request.env['tech_purchase.tech_purchase'].search([]),
#         })

#     @http.route('/tech_purchase/tech_purchase/objects/<model("tech_purchase.tech_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_purchase.object', {
#             'object': obj
#         })
