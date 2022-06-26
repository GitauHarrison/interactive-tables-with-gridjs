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


@app.route('/server-side-table')
def server_side_table():
    users = User.query
    if users.count() >= 10000:
        users = users.limit(10000)
    else:
        create_fake_users(500)
        print("All users are created: ", users.count())
    return render_template(
        'server_side_table.html',
        users=users,
        title='Server-side table')


@app.route('/server-side-table-data')
def server_side_table_data():
    query = User.query

    # Search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            User.name.like(f'%{search}%'),
            User.email.like(f'{search}%')
        ))
    total = query.count()

    # Sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['name', 'email', 'age']:
                name = 'name'
            col = getattr(User, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)

    # Pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)

    # Response
    return {
        'data': [user.to_dict() for user in query.all()],
        'total': total
    }
