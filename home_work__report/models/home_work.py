# -*- coding: utf-8 -*-
import datetime
import time
import calendar
from odoo import models, fields, api

class home_work__report(models.Model):
    _name = 'home_work__report.home_work'

    subject = fields.Char('Subject')
    class_type = fields.Selection([('Nursery', 'Nursery'),('Junior KG', 'Junior KG'),('Senior KG','Senior KG'),('I','I'),('II','II'),('III','III'),('IV','IV'),
                                   ('V','V')], string="Class" , default='All',store=True)
    section = fields.Selection([('A', 'A'),('B','B'),('C','C')], string="Section" , default='',store=True)
    homework = fields.Text('Home Work')
    startdate = fields.Date('Start Date')
    enddate = fields.Date('End Date')