# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.client import Client

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_client(app):
    app.login(username="admin", password="secret")
    app.create_client(Client(firstname="firstqweqwe", middlename="middlejhfghkdjfhfgdf", lastname="lastjvhfdkjghg", nickname="nicjfhdjkghf",
                           title="titltfjdjfhjdhgh", company="companyhdjfkshkfs", address="adreddkdfkjgldfjgfdjkfjgldfkjg", homephone="85654752453426",
                           mobilephone="987988989", workphone="1074567456757555", fax="2475858585", emaleone="hdhfwghfg@hgjhfg.com",
                           emailtwo="fhgerhgjrhhh@ffjgjg.com", emailthree="fhfh@.com", homepage="qwe", daybirthday="2", monthbirthday="February", yearbirthday="2006", annday="5", annmonth="July", annyear="2008"))
    app.logout()

def test_add_empty_client(app):
    app.login(username="admin", password="secret")
    app.create_client(Client(firstname="", middlename="",
                               lastname="", nickname="",
                               title="", company="",
                               address="", homephone="",
                               mobilephone="", workphone="", fax="",
                               emaleone="",
                               emailtwo="", emailthree="", homepage="",
                               daybirthday="-", monthbirthday="-", yearbirthday="-", annday="-",
                               annmonth="-", annyear="-"))
    app.logout()


