from model.client import Client

def test_modify_client_firstname(app):
    if app.client.count() == 0:
        app.client.create(Client(firstname="test"))
    app.client.modify_first_client(Client(firstname="New firstname"))

def test_modify_client_middlename(app):
    if app.client.count() == 0:
        app.client.create(Client(middlename="test"))
    app.client.modify_first_client(Client(middlename="New middlename"))