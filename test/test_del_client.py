from model.client import Client


def test_delete_first_client(app):
    if app.client.count() == 0:
        app.client.create(Client(firstname="testfirstname"))
    app.client.delete_first_client()
