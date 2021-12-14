from typing import Sized
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Cupcake app."""

class Cupcake(db.Model):
    '''Cupcake model'''

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, default = 'https://tinyurl.com/demo-cupcake')
    
    def serialize_cupcake(self):
        '''Serialize a cupcake SQLAlchemy obj to a dictionary'''

        return {
            "id" : self.id,
            "flavor" : self.flavor,
            "size" : self.size,
            "rating": self.rating,
            "image" : self.image
        }
