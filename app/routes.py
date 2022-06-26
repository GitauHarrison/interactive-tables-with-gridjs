from app import app
from flask import render_template
from app.models import User
from create_fake_users import create_fake_users


@app.route('/')
def basic_table():
    users = User.query
    if users.count() >= 100:
        users = users.limit(100)
    else:
        create_fake_users(10)
        print("All users are created: ", users.count())
    return render_template('basic_table.html', users=users)
