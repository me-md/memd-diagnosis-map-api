from app import db
from sqlalchemy.dialects.postgresql import JSON


class Condition(db.Model):
    __tablename__ = 'conditions'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String())
    name = db.Column(db.String())


    def __init__(self, state, name):
        self.state = state
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)
