# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
import ast
from datetime import datetime
logger = logging.getLogger(__name__)


class Contactos(models.Model):
    _inherit = 'res.partner'

    campaign_ids = fields.Many2many('campaign', string='Campaigns')


class Campaign(models.Model):
    _name = 'campaign'
    _parent_store=True
    _parent_name='parent_id'

    name= fields.Char(string='Name')
    partner_ids = fields.Many2many('res.partner', string='Contacts')
    campaign_type = fields.Selection([
        ('email', 'Email'),
        ('physical_delivery', 'Physical Delivery'),
        ('hand_delivered', 'Hand Delivered')
    ], string='Campaign Type')
    delivered = fields.Boolean(string='Delivered')
    delivered_date = fields.Date(string="Delivered Date")
    parent_id = fields.Many2one('campaign',string='Parent Campaign',ondelete='restrict',index=True)
    child_ids = fields.One2many('campaign','parent_id',string='Hijos',)
    parent_path= fields.Char(index=True)
    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('hierarchy error')


class marketingAutomation(models.Model):
    _inherit = 'marketing.campaign'

    campaignVariable_id = fields.Many2one('campaign',string='Campaign')
    #This method on change of state (when someone starts the campaign)
    #gets every target contact and add to the campaign_ids field the campaignVariable_id value
    def write(self, vals):
        res = super(marketingAutomation,self).write(vals)
        currentState=vals.get("state",False)
        if currentState == 'running' and self.campaignVariable_id:
            self.campaignVariable_id.delivered = True
            self.campaignVariable_id.delivered_date = datetime.now()
            domainMarketing = ast.literal_eval(self.domain)
            contacts = self.env['res.partner'].search(domainMarketing)
            for a in contacts:
                self.env['marketing.participant'].create({
                    'name': a.name,
                    'enterprise': a.parent_id.name,
                    'phone': a.phone,
                    'street': a.street,
                    'zip': a.zip,
                    'city': a.city,
                    'state': a.state,
                })
                a.write({'campaign_ids': [(4, self.campaignVariable_id.id)]})
        return res

    
class marketingAutomation(models.Model):
    _inherit = 'marketing.participant'

    name = fields.Char(string="Name")
    enterprise = fields.Char(string="Enterprise")
    phone = fields.Char(string="Phone")
    street = fields.Char(string="Street")
    zip = fields.Char(string="Zip")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
