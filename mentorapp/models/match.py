from mentorapp.app import db


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mentor = db.Column(db.Integer, db.ForeignKey('user.id'))
    mentee = db.Column(db.Integer, db.ForeignKey('user.id'))
