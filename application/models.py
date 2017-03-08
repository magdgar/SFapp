from app import db


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