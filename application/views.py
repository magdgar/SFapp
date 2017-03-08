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


@app.route('/profile/<first_name>')
def profile(first_name):
    user = User.query.filter_by(first_name=first_name).first()
    return render_template('profile.html', user=user)


@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.json['first_name'], request.json['last_name'],
                request.json['birth_date'], request.json['zip_code'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update_user/<user_id>', methods=['PATCH'])
def update_user(user_id):
    json_user = {
        "first_name": request.json['first_name'],
        "last_name": request.json['last_name'],
        "birth_date": request.json['birth_date'],
        "zip_code": request.json['zip_code'],
    }
    db.session.query(User).filter_by(id=user_id).update(json_user)
    db.session.commit()
    return render_template('profile.html', user=json_user)


@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter(User.id == user_id).first()
    db.session.delete(user)
    db.session.commit()
    return render_template('profile.html', user=user)
