from flask import render_template
from app import app, db
from app.models import User
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
    user = User(request.form['first_name'], request.form['last_name'],
                request.form['birth_date'], request.form['zip_code'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
