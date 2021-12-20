# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'exemplo de odoo basico'
    _sql_constraints = [('nome_unico', 'unique(name)', 'Non se pode repetir o nome')]

    name = fields.Char(string="Titulo!")
    descripcion = fields.Text(string="A Descripcion")
    alto_cm = fields.Integer(string="Alto en cm")
    longo_cm = fields.Integer(string="Longo en cm")
    ancho_cm = fields.Integer(string="Ancho en cm")
    volume = fields.Float(compute="_volume", store=True)
    peso = fields.Float(digits=(6, 2), string="Peso en Kg.s", default=2.7)
    moeda_id = fields.Many2one('res.currency', domain="[('position','=','after')]")
    moeda_texto = fields.Char(related="moeda_id.currency_unit_label",
                                 string="Moeda en formato texto", store=True)
    moeda_euro_id = fields.Many2one('res.currency',
                default=lambda self: self.env['res.currency'].search([('name', '=', "EUR")],
                limit=1))
    gasto_euros = fields.Monetary("Gasto en Euros", 'moeda_euro_id')
    gasto_moeda_seleccionada = fields.Monetary("Gasto en Moeda Seleccionada", 'moeda_id')
    densidade = fields.Float(compute="_densidade", store=True)
    autorizado = fields.Boolean(string="Autorizado")
    sexo_traducido = fields.Selection([("Hombre","Home"),("Mujer","Muller"),("Otros","Outros")],string="Sexo")
    literal = fields.Char(store=False)
    foto = fields.Binary(string='Foto')
    adxunto_nome = fields.Char(string="Nome Adxunto")
    adxunto = fields.Binary(string="Arquivo adxunto")

    @api.depends('alto_cm', 'longo_cm', 'ancho_cm')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_cm) * float(rexistro.longo_cm) * float(rexistro.ancho_cm)


    @api.depends("volume" , "peso" )
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = 100* (float(rexistro.peso) / float(rexistro.volume))
            else:
                rexistro.densidade = 0

    @api.onchange('alto_cm')
    def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_cm > 7:
                rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_cm
            else:
                rexistro.literal = ""

    @api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
    def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 4:
                raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)

    def _cambia_campo_sexo(self, rexistro):
        rexistro.sexo_traducido = "Hombre"



