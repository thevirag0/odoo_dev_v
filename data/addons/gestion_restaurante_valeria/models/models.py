from odoo import models, fields, api

<<<<<<< HEAD

class gestion_restaurante_valeria(models.Model):
class gestion_restaurante_valeria(models.Model):
    _name = 'gestion_restaurante_valeria.gestion_restaurante_valeria'
    _description = 'gestion_restaurante_valeria.gestion_restaurante_valeria'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


=======
>>>>>>> c96603b (commit clase 30/01)
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

