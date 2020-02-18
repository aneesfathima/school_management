# -*- coding: utf-8 -*-

import datetime
import time
import calendar
from odoo import models, fields, api

class sheet(models.Model):
    _name = 'attendance.sheet'

    name = fields.Char(string="Student Name")
    enrollment = fields.Integer(string="Enrollment Number")
    class_type = fields.Selection([('Nursery', 'Nursery'),('Junior KG', 'Junior KG'),('Senior KG','Senior KG'),('I','I'),('II','II'),('III','III'),('IV','IV'),
                                   ('V','V')], string="Class" , default='All',store=True)
    section = fields.Selection([('A', 'A'),('B','B'),('C','C')], string="Section" , default='',store=True)
    period = fields.Selection([('1', '1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')], string="Period" , default='',store=True)
    date = fields.Date(String="Date")
    active = fields.Boolean(string='Present')
    absent = fields.Boolean(string='Absent')

