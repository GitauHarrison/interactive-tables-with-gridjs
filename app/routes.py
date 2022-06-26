from app import app, db
from flask import render_template, request, abort
from app.models import User
from create_fake_users import create_fake_users


def fake_users():
    """Create fake users and limit them to 10000."""
    db_users = User.query
    if db_users.count() >= 10000:
        all_users = db_users.limit(10000)
    else:
        create_fake_users(500)
    return all_users


@app.route('/')
@app.route('/index')
def index():
    """Render the index page."""
    return render_template('index.html', title='Home')


@app.route('/bootstrap-table')
def bootstrap_table():
    """Render bootstrap table."""
    all_users = fake_users()
    return render_template(
        'bootstrap_table.html',
        users=all_users,
        title='Bootstrap Table')


@app.route('/basic-table')
def basic_table():
    """
    Basic table with few features.
    All data loaded and displayed at once
    """
    users = fake_users()
    return render_template(
        'basic_table.html',
        users=users,
        title='Basic Table')


@app.route('/ajax-table')
def ajax_table():
    """
    Render empty table.
    Data will be loaded via AJAX afterwards.
    """
    users = fake_users()
    return render_template(
        'ajax_table.html',
        users=users,
        title='AJAX Table')


@app.route('/ajax-table-data')
def ajax_data():
    """
    Return a dictionary of users' data
    """
    return {'data': [user.to_dict() for user in User.query.all()]}


@app.route('/server-side-table')
def server_side_table():
    """
    Users data displayed on request.
    If page 1 is requested, data for ony that page will be loaded.
    """
    users = fake_users()
    return render_template(
        'server_side_table.html',
        users=users,
        title='Server-side table')


@app.route('/server-side-table-data')
def server_side_table_data():
    """
    Add search, sort and pagination functionalities
    in the server
    """
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
        'data': [user.to_dict() for user in query],
        'total': total
    }


@app.route('/editable-table')
def editable_table():
    """
    App user should be able to edit select fields.
    The edited data will be saved in the database.
    """
    users = fake_users()
    return render_template(
        'editable_table.html',
        users=users,
        title='Editable Table')


@app.route('/editable-table-update', methods=['POST'])
def editable_table_update():
    """
    Update user data in the database.
    """
    data = request.get_json()
    if 'id' not in data:
        abort(400)
    user = User.query.get(data['id'])
    fields = ['name', 'age', 'address', 'phone', 'email']
    for field in fields:
        if field in data:
            setattr(user, field, data[field])
    db.session.commit()
    return '', 204
