from odoo import models, fields, api

class platos_valeria(models.Model):
    _name = 'gestion_restaurante_valeria.platos_valeria'
    _description = 'gestion_restaurante_valeria.lo de los platos'

    name = fields.Char()
    description = fields.Text(
    )

    # @api.depends('name')
    # def _value_pc(self):
    #     for record in self:
    #         if not record.description: 
    #             record.description = record.name + "_Mi descripcion"
            # record.value2 = float(record.value) /100

