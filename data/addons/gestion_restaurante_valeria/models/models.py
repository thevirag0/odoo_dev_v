from odoo import models, fields, api

class gestion_restaurante_valeria(models.Model):
    _name = 'gestion_restaurante_valeria.gestion_restaurante_valeria'
    _description = 'gestion_restaurante_valeria.gestion_restaurante_valeria'

    name = fields.Char()
    description = fields.Text()

@api.depends('value')
def _value_pc(self):
    for record in self:
        record.value2 = float(record.value) / 100

class platos_valeria(models.Model):
    _name = 'gestion_restaurante_valeria.platos_valeria'
    _description = 'Modelo de Platos para Gestión de Restaurante'

    name = fields.Char()
    description = fields.Text()