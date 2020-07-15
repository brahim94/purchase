# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class Tech_purchase(models.TransientModel):

    _inherit = "res.config.settings"

    first_limit = fields.Monetary('Seuil 1')
    second_limit = fields.Monetary('Seuil 2')


class Tech_purchase_oreder(models.Model):

    _inherit = "purchase.order"

    state = fields.Selection([
        ('draft', 'RFQ'),
        ('sent', 'RFQ Sent'),
        ('verifie', 'Commande vérifiée'),
        ('aprouve', 'Commande approuvée'),
        ('valide', 'Commande validée'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)

    def action_verifie(self):
        for rec in self:
            rec.state = 'verifie'
    
    def action_aprouve(self):
        for rec in self:
            rec.state = 'aprouve'

    def action_valide(self):
        for rec in self:
            rec.state = 'valide'