# -*- coding:utf-8 -*-

import logging
from odoo.exceptions import ValidationError
from odoo import fields, models, api

logger = logging.getLogger(__name__)
class Productos(models.Model):
    _inherit = 'product.template'

    referencias = fields.Char(string='Referencias_Variantes')

    def lengthList(self,lst):
        for element in lst:
            if len(element) > 50:
                return True
        return False

    @api.depends("name")
    def importacionRef(self):
        for a in self:
            if a.referencias:
                x = self.env['product.product'].search([('name','=', a.name)])
                y = a.referencias.split(',')
                if ',' not in a.referencias:
                    raise ValidationError("Cada valor debe estar separado por comas")
                elif ' ' in a.referencias:
                    raise ValidationError("No debe contener espacios el campo.")
                elif self.lengthList(y):
                    raise ValidationError("Alguna referencia es mayor a 50 caracteres.")
                elif len(y) != len(set(y)):
                    raise ValidationError("Algun valor esta repetido")
                elif len(y) != len(x):
                    raise ValidationError("Faltan referencias")
                try:
                    contador = 0
                    for b in x:
                        b['default_code'] = y[contador]
                        contador=contador+1
                    a.referencias = False
                except:
                    raise ValidationError("Algo falló")
    @api.model
    def create(self, vals):
        result = super(Productos, self).create(vals)
        result.importacionRef()
        return result

    