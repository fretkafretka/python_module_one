# -*- coding: utf-8 -*-
import pytest
from fixture.application import ApplicationGroup
from model.group import Group


@pytest.fixture
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="group098", header="wqteitriuyeiureir", footer="gdfdjhgdjhfjkhdfkg"))
    app.logout()

def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()




        

