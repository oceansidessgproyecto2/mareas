from odoo import models, fields, api
class prediccion(models.Model):
 _name = 'mareas.prediccion'
 _description = 'prediccion de mareas en un rango de fechas'

 fecha_inicio = fields.Date(string="Fecha de inicio")
 fecha_final = fields.Date(string="Fecha final")

class api_key(models.Model):
 _name = 'mareas.apikey'
 _description = "API key de mareas."

 token = fields.Char(string="Token")