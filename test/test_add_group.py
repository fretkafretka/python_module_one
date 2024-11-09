# -*- coding: utf-8 -*-
from model.group import Group

def test_group(app):
    app.group.create(Group(name="group098", header="wqteitriuyeiureir", footer="gdfdjhgdjhfjkhdfkg"))

def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))







        

