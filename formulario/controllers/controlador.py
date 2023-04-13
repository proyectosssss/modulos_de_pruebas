# -*- coding: utf-8 -*-
import logging
import odoo.http as http
from odoo.http import request
from werkzeug.utils import redirect
logger = logging.getLogger(__name__)


class your_class(http.Controller):
     @http.route('/confirm',type='http', auth='public', website=True, methods=['POST'],csrf=False)
     def controller1(self, **kw):
          args = { 'name':kw.get('name'),'email':kw.get('email') }
          return request.render('formulario.confirm',{'informacion': args})



     @http.route('/confirmed', type='http', auth='public', website=True, methods=['POST'],csrf=False)
     def controller2(self, **kw):
          request.env['crm.lead'].create({
               'name': kw.get('name'),
               'email_from': kw.get('email'),
          })
          return redirect('/contactus-thank-you')
