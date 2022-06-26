from app import app, db
from flask import render_template, request
from app.models import User
from create_fake_users import create_fake_users


@app.route('/basic-table')
def basic_table():
    """Basic table with few features."""
    users = User.query
    if users.count() >= 10000:
        users = users.limit(1000)
        print("All users are shown.", users.count())
    else:
        create_fake_users(500)
        print("All users are created: ", users.count())
    return render_template(
        'basic_table.html',
        users=users,
        title='Basic Table')


@app.route('/ajax-table')
def ajax_table():
    users = User.query
    if users.count() >= 10000:
        users = users.limit(10000)
    else:
        create_fake_users(500)
        print("All users are created: ", users.count())
    return render_template(
        'ajax_table.html',
        users=users,
        title='AJAX Table')


@app.route('/ajax-table-data')
def ajax_data():
    return {'data': [user.to_dict() for user in User.query.all()]}
