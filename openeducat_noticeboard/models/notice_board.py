# -*- coding: utf-8 -*-
import datetime
import time
import calendar
from odoo import http, fields
from odoo.http import request
from odoo import models, fields, api

class openeducat_noticeboard(models.Model):
    _name = 'openeducat_noticeboard.noticeboard'

    title = fields.Char('Title', required=True)
    content = fields.Text('Content')
    time = fields.Datetime('Date And Time')


