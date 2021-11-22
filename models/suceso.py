# -*- coding: utf-8 -*-

from odoo import models, fields, api


class suceso(models.Model):
    _name = 'odoo_basico.suceso'
    _description = 'exemplo de odoo basico'


    name = fields.Char(string="Titulo!")
    descripcion = fields.Text(string="A Descripcion")
    nivel = fields.Selection([('Baixo', 'Baixo'), ('Medio', 'Medio'), ('Alto', 'Alto')], string='Nivel')
    data_hora = fields.Datetime(string="Data e Hora", default=lambda self: fields.Datetime.now())