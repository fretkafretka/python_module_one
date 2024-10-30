# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from client import Client


class AddClient(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
            
    def test_add_client(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_client(wd, Client(firstname="firstqweqwe", middlename="middlejhfghkdjfhfgdf", lastname="lastjvhfdkjghg", nickname="nicjfhdjkghf",
                           title="titltfjdjfhjdhgh", company="companyhdjfkshkfs", address="adreddkdfkjgldfjgfdjkfjgldfkjg", homephone="85654752453426",
                           mobilephone="987988989", workphone="1074567456757555", fax="2475858585", emaleone="hdhfwghfg@hgjhfg.com",
                           emailtwo="fhgerhgjrhhh@ffjgjg.com", emailthree="fhfh@.com", homepage="qwe", daybirthday="2", monthbirthday="February", yearbirthday="2006", annday="5", annmonth="July", annyear="2008"))
        self.logout(wd)

    def test_add_empty_client(self):
            wd = self.wd
            self.login(wd, username="admin", password="secret")
            self.create_client(wd, Client(firstname="", middlename="",
                               lastname="", nickname="",
                               title="", company="",
                               address="", homephone="",
                               mobilephone="", workphone="", fax="",
                               emaleone="",
                               emailtwo="", emailthree="", homepage="",
                               daybirthday="-", monthbirthday="-", yearbirthday="-", annday="-",
                               annmonth="-", annyear="-"))
            self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_client(self, wd, client):
        self.open_client_page(wd)
        # fill client form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(client.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(client.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(client.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(client.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(client.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(client.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(client.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(client.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(client.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(client.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(client.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(client.emaleone)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(client.emailtwo)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(client.emailthree)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(client.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(client.daybirthday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(client.monthbirthday)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(client.yearbirthday)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(client.annday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(client.annmonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(client.annyear)
        # create client
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_home_page(wd)

    def open_client_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
           
    def tearDown(self):
        self.wd.quit()
       

if __name__ == "__main__":
    unittest.main()
