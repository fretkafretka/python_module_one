# -*- coding: utf-8 -*-

from model.client import Client

def test_add_client(app):
    app.client.create(Client(firstname="firstqweqwe", middlename="middlejhfghkdjfhfgdf", lastname="lastjvhfdkjghg", nickname="nicjfhdjkghf",
                             title="titltfjdjfhjdhgh", company="companyhdjfkshkfs", address="adreddkdfkjgldfjgfdjkfjgldfkjg", homephone="85654752453426",
                             mobilephone="987988989", workphone="1074567456757555", fax="2475858585", emaleone="hdhfwghfg@hgjhfg.com",
                             emailtwo="fhgerhgjrhhh@ffjgjg.com", emailthree="fhfh@.com", homepage="qwe", bday="2", bmonth="February", byear="2006", aday="5", amonth="July", ayear="2008"))

def test_add_empty_client(app):
    app.client.create(Client(firstname="", middlename="",
                             lastname="", nickname="",
                             title="", company="",
                             address="", homephone="",
                             mobilephone="", workphone="", fax="",
                             emaleone="",
                             emailtwo="", emailthree="", homepage="",
                             bday="-", bmonth="-", byear="-", aday="-",
                             amonth="-", ayear="-"))



