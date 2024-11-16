from model.client import Client


def test_delete_first_client(app):
    if app.client.count() == 0:
        app.client.create(Client(firstname="testfirstname", middlename="testmiddlename", lastname="testlastname", nickname="testnickname", title="testtitle",
                                 company="testcompany",address="testaddres",homephone="234324",mobilephone="45545", workphone="23432",fax="3243",emaleone="rerere", emailtwo="323dffdf", emailthree="5555",
                                 homepage="ddfk",daybirthday="-",monthbirthday="-",yearbirthday="-",annday="-", annmonth="-", annyear="-"))
    app.client.delete_first_client()
