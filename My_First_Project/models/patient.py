from odoo import api, fields, models
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Patient Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender', tracking=True)
    ref = fields.Char(string='Reference', default='patients', tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    note = fields.Text(string='Note')
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirmed'),
        ('approve','Approved'),
        ('cancel','Cancelled')
    ], string='Status', default='draft')

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

