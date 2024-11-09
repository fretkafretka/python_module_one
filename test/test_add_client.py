# -*- coding: utf-8 -*-

from model.client import Client

def test_add_client(app):
    app.client.create(Client(firstname="firstqweqwe", middlename="middlejhfghkdjfhfgdf", lastname="lastjvhfdkjghg", nickname="nicjfhdjkghf",
                             title="titltfjdjfhjdhgh", company="companyhdjfkshkfs", address="adreddkdfkjgldfjgfdjkfjgldfkjg", homephone="85654752453426",
                             mobilephone="987988989", workphone="1074567456757555", fax="2475858585", emaleone="hdhfwghfg@hgjhfg.com",
                             emailtwo="fhgerhgjrhhh@ffjgjg.com", emailthree="fhfh@.com", homepage="qwe", daybirthday="2", monthbirthday="February", yearbirthday="2006", annday="5", annmonth="July", annyear="2008"))

def test_add_empty_client(app):
    app.client.create(Client(firstname="", middlename="",
                             lastname="", nickname="",
                             title="", company="",
                             address="", homephone="",
                             mobilephone="", workphone="", fax="",
                             emaleone="",
                             emailtwo="", emailthree="", homepage="",
                             daybirthday="-", monthbirthday="-", yearbirthday="-", annday="-",
                             annmonth="-", annyear="-"))



