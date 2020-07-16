# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class  ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    first_limit = fields.Monetary('Seuil 1')
    second_limit = fields.Monetary('Seuil 2')
    limit_id = fields.Many2one('purchase.order', string="Seuil 1 ID")

    @api.model
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('tech_purchase.first_limit', int(self.first_limit))
        set_param('tech_purchase.second_limit', int(self.second_limit))


    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res['first_limit'] = int(get_param('tech_purchase.first_limit'))
        res['second_limit'] = int(get_param('tech_purchase.second_limit'))
        return res


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
    limit = fields.One2many('res.config.settings','limit_id', string="Seuils")
    first_limit_id = fields.Monetary(related='limit.first_limit')
    second_limit_id = fields.Monetary(related='limit.second_limit')

    def action_verifie(self):
        for rec in self:
            rec.state = 'verifie'
    
    def action_aprouve(self):
        for rec in self:
            rec.state = 'aprouve'

    def action_valide(self):
        for rec in self:
            rec.state = 'valide'