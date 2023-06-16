# -*- coding:utf-8 -*-


from odoo import fields, models, api

class Stages(models.Model):
    _name="new.stage"
    _inherit = 'crm.stage'
    
    text = fields.Char(string="Description")
   

