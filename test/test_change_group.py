from model.group import Group

def test_change_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.change(Group(name="groupqwerty", header="123", footer="opopopop"))
