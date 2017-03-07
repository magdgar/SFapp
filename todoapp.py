from flask import Flask, render_template
from flask import redirect
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/todoapp'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    birth_date = db.Column(db.Date())
    zipcode = db.Column(db.String(10))

    def __init__(self, first_name, last_name, birth_date, zipcode):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.zipcode = zipcode

    def __repr__(self):

        return '<User %r>' % self.first_name


@app.route('/')
def index():
    myUser = User.query.all()
    oneItem = User.query.filter_by(first_name='root').first()
    return render_template('add_user.html', myUser=myUser, oneItem=oneItem)


@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['first_name'], request.form['last_name'],
                request.form['birth_date'], request.form['zip_code'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()
