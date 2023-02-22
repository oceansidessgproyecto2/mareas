# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests
import json

# class Coches(http.Controller):
#     @http.route('/coches/coches', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coches/coches/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('coches.listing', {
#             'root': '/coches/coches',
#             'objects': http.request.env['coches.coches'].search([]),
#         })

#     @http.route('/coches/coches/objects/<model("coches.coches"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coches.object', {
#             'object': obj
#         })
class Mareas(http.Controller):
     @http.route('/mareas',methods=['GET'], auth='user')
     def index(self, **kw):
         return request.render("mareas.index", {})
     @http.route('/mareasoutput',methods=['GET'], auth='user')
     def form(self, **kw):
          url = "http://51.140.136.62:8010/marea.php?dinnie="+kw.get("dinnie")+"&finnie="+kw.get("finnie");
          headers = {'X-Marea-Auth': 'hadad3l0sd13nt3s'}

          r = requests.get(url,headers=headers)
          res = json.loads(r.text)["msg"]
          return request.render("mareas.showa", {'res':res})