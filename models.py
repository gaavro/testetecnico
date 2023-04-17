from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

class Expression(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expression = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Expression {self.id} {self.expression}>'