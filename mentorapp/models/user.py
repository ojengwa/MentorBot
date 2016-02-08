# from mentorapp.app import db
from flask.ext.login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String())
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(36))
    last_name = db.Column(db.String(36))
    avatar = db.Column(db.String(256), unique=True)
    is_staff = db.Column(db.Boolean, default=False)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.email
