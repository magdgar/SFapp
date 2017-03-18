from application import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    birth_date = db.Column(db.Date())
    zip_code = db.Column(db.String(10))

    def __init__(self, first_name, last_name, birth_date, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.zip_code = zip_code

    def __repr__(self):
        return '<User %r>' % self.first_name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}