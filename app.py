from flask import Flask, request, render_template, jsonify
from models import db, connect_db, Cupcake, serialize

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

"""Flask app for Cupcakes"""

@app.route('/api/cupcakes')
def get_all_cupcakes():
    '''Get a list of all cupcakes'''

    cupcakes = Cupcake.query.all()
    serialized = [serialize(cupcake) for cupcake in cupcakes]
    return (jsonify(cupcakes=serialized))

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_single_cupcake(cupcake_id):
    '''Get data about single cupcake'''

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize(cupcake)

    return (jsonify(cupcake = serialized))

@app.route('/api/cupcakes', methods = ["POST"])
def create_cupcake():
    '''Create a cupcake with flavor, size, rating and image data'''
    
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"] or None
    
    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    
    db.session.add(cupcake)
    db.session.commit()

    serialized = serialize(cupcake)

    return (jsonify(cupcake=serialized), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    '''Update cupcake'''
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    cupcake.flavor = request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]
    cupcake.image = request.json["image"]
   
    db.session.add(cupcake)
    db.session.commit()

    serialized = serialize(cupcake)
    
    return jsonify(cupcake = serialized)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    '''Delete cupcake '''

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.delete

    return jsonify(msg='Cupcake deleted')


