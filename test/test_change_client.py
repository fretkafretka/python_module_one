from model.client import Client


def test_change_client(app):
    app.session.login(username="admin", password="secret")
    app.client.change(Client(firstname="Yulia", middlename="qweqwe", lastname="last qwe", nickname="nic123",
                             title="titl123", company="company44", address="ad555", homephone="85654752453426",
                             mobilephone="987988989", workphone="1074567456757555", fax="2475858585", emaleone="hdhfwghfg@hgjhfg.com",
                             emailtwo="fpopopopffjgjg.com", emailthree="klklfh@.com", homepage="qwe", daybirthday="2", monthbirthday="February", yearbirthday="2006", annday="5", annmonth="July", annyear="2009"))
    app.session.logout()