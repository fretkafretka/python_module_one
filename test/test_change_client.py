from model.client import Client


def test_change_client(app):
    app.client.change(Client(firstname="Yulia", middlename="qweqwe", lastname="last qwe", nickname="nic123",
                             title="titl123", company="company44", address="ad555", homephone="85654752453426",
                             mobilephone="987988989", workphone="1074567456757555", fax="2475858585", emaleone="hdhfwghfg@hgjhfg.com",
                             emailtwo="fpopopopffjgjg.com", emailthree="klklfh@.com", homepage="qwe", bday="2", bmonth="February", byear="2006", aday="5", amonth="July", ayear="2009"))
