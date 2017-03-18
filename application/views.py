from flask import render_template, jsonify
from application import app, db
from application.models import User
from flask import request


@app.route('/')
def index():
    myUser = User.query.all()
    oneItem = User.query.filter_by(first_name='root').first()
    return render_template('add_user.html', myUser=myUser, oneItem=oneItem)


@app.route('/user', methods=['GET', 'POST'], defaults={'user_id': None})
@app.route('/user/<user_id>', methods=['GET', 'PATCH', 'DELETE'])
def user_handler(user_id):
    return {
            'GET':  _get_user,
            'POST':  _post_user,
            'PATCH': _update_user,
            'DELETE': _delete_user
        }[request.method](user_id)


def _get_user(user_id):
    if user_id is None:
        return jsonify({"data": [user.as_dict() for user in db.session.query(User).all()]})
    else:
        return jsonify({"user": db.session.query(User).filter_by(id=user_id).first().as_dict()})


def _post_user(args):
    if request is not None:
        user = User(request.json['first_name'], request.json['last_name'],
                request.json['birth_date'], request.json['zip_code'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"user": user.as_dict()})


def _update_user(user_id):
    json_user = {
        "first_name": request.json['first_name'],
        "last_name": request.json['last_name'],
        "birth_date": request.json['birth_date'],
        "zip_code": request.json['zip_code'],
    }
    db.session.query(User).filter_by(id=user_id).update(json_user)
    db.session.commit()
    return _get_user(user_id)


def _delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({"user": user.as_dict()})
