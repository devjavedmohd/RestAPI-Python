from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# app.config['SQLAlchemy_TRACK_MODIFICATION'] = False
# from application import db - in terminal type 
# :python > then 'from application imoprt db' 
# that will be in .venv/Scripts/activate folder 

db = SQLAlchemy(app)

# Class (table) drink for database connections
class Drink(db.Model):
    # Columns which store data in the sqlite database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.name} - {self.description}"

# setting routes
@app.route('/')
def index():
    return 'Hello, world'

# setting route for drinks page to get content
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
        
    return {"drinks" : output}


# setting route for drinks > id page to get content
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

# POST /drinks 
@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}



@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {'error': 'drink not found'}
    db.session.delete(drink)
    db.session.commit()
    return {'message': 'drink was deleted'}


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables

    print("Starting Flask app...")
    app.run(debug=True)