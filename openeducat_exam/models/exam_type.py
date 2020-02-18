# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields


class OpExamType(models.Model):
    _name = "op.exam.type"
    _description = "Exam Type"

    name = fields.Char('Exam Name', size=256, required=True)
    code = fields.Char('Exam Code', size=16)
    class_type = fields.Selection([('Nursery', 'Nursery'),('Junior KG', 'Junior KG'),('Senior KG','Senior KG'),('I','I'),('II','II'),('III','III'),('IV','IV'),
                                   ('V','V')], string="Class" , default='All',store=True)
    exam_type = fields.Selection([('Term I', 'Term I'),('Term II', 'Term II'),('Term III','Term III'),('Cycle Test 1','Cycle Test 1'),('Cycle Test 2','Cycle Test 2'),('Cycle Test 3','Cycle Test 3'),('Cycle Test 4','Cycle Test 4'),
                                   ('Cycle Test 5','Cycle Test 5'),('Half Yearly','Half Yearly'),('Annual','Annual')], string="Select Term" ,store=True)

    _sql_constraints = [
        ('unique_exam_type_code',
         'unique(code)', 'Code should be unique per exam type!')]
