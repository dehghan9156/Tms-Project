from odoo import models, fields, api


class Car(models.Model):
    _name = 'transport.car'
    _description = 'transport.car'

    car_model = fields.Char(string='Car Model',translate=True)
    car_tag = fields.Char(string='Car Model',required=True,translate=True)
    year_of_const = fields.Date(string='Year of construction' , help="Year of construction.")
    age = fields.Char(string='Car age', default="0")
    car_drivers = fields.Many2many('res.partner',string='Car Driver')

    _sql_constraints = [
        ('car_tag_uniq','unique(car_tag)','Car tag must be unique !')
    ]



    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
