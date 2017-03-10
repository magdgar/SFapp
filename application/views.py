from flask import render_template
from application import app, db
from application.models import User
from flask import redirect
from flask import request
from flask import url_for


@app.route('/')
def index():
    myUser = User.query.all()
    oneItem = User.query.filter_by(first_name='root').first()
    return render_template('add_user.html', myUser=myUser, oneItem=oneItem)


@app.route('/user', methods=['GET', 'POST'], defaults={'user_id': None})
@app.route('/user/<user_id>', methods=['GET', 'PATCH', 'DELETE'])
def user_handler(user_id):
    return {
        'GET':  _get_user(user_id),
        'POST':  _post_user(),
        'PATCH': _update_user(user_id),
        'DELETE': _delete_user(user_id)
    }[request.method]


def _get_user(user_id):
    if user_id is None:
        return db.session.query(User).all()
    else:
        return db.session.query(User).filter_by(id=user_id).first()


def _post_user():
    user = User(request.json['first_name'], request.json['last_name'],
                request.json['birth_date'], request.json['zip_code'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


def _update_user(user_id):
    json_user = {
        "first_name": request.json['first_name'],
        "last_name": request.json['last_name'],
        "birth_date": request.json['birth_date'],
        "zip_code": request.json['zip_code'],
    }
    db.session.query(User).filter_by(id=user_id).update(json_user)
    db.session.commit()
    return render_template('profile.html', user=json_user)


def _delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return render_template('profile.html', user=user)
