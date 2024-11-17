from selenium.webdriver.common.keys import Keys


class ClientHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, client):
        wd = self.app.wd
        self.open_client_page()
        self.fill_client_form(client)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.open_home_page()

    def change(self, client):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_client_form(client)
        wd.find_element_by_name("update").click()
        self.open_home_page()

    def fill_client_form(self, client):
        wd = self.app.wd
        self.change_field_value("firstname", client.firstname)
        self.change_field_value("middlename", client.middlename)
        self.change_field_value("middlename", client.middlename)
        self.change_field_value("lastname", client.lastname)
        self.change_field_value("nickname", client.nickname)
        self.change_field_value("title", client.title)
        self.change_field_value("company", client.company)
        self.change_field_value("address", client.address)
        self.change_field_value("home", client.homephone)
        self.change_field_value("mobile", client.mobilephone)
        self.change_field_value("work", client.workphone)
        self.change_field_value("fax", client.fax)
        self.change_field_value("email", client.emaleone)
        self.change_field_value("email2", client.emailtwo)
        self.change_field_value("email3", client.emailthree)
        self.change_field_value("homepage", client.homepage)
        self.change_field_value("bday", client.bday)
        self.change_field_value("bmonth", client.bmonth)
        self.change_field_value("byear", client.byear)
        self.change_field_value("aday", client.aday)
        self.change_field_value("amonth", client.amonth)
        self.change_field_value("ayear", client.ayear)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            if text is not None:
                return
            else:
                wd = self.app.wd
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def delete_first_client(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_client()
        # scroll
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_home_page()

    def select_first_client(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_client_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def modify_first_client(self, new_client_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_client()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill client form
        self.fill_client_form(new_client_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))