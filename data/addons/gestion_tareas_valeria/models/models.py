from odoo import models, fields, api


class gestion_tareas_valeria(models.Model):
     _name = 'gestion_tareas_valeria.gestion_tareas_valeria'
     _description = 'gestion_tareas_valeria.gestion_tareas_valeria'

     nombre = fields.Char()
     descripcion = fields.Text()

@api.depends('value')
def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100