Creating Environment and running environment:
	1. python -m venv .venv
	2. .venv\Scripts\activate (to activate)
	3. pip install flask flask-sqlalchamey (to use flask/sqlalchamey for database)
	4. set FLASK_APP=application.py
	5. set FLASK_ENV=development
	6. flask run

To run db in windows:
Run following commands
$ flask shell                                                                                   
>>> from application import db                                                                  
>>> with app.app_context():                                                                     
...     db.create_all()                                                                         
...                                                                                             
>>>                                                                                             
>>> drink = Drink(name="Grape Soda", description="Tastes like grapes")                          
>>> drink                                                                                       
Grape Soda - Tastes like grapes                                                                 
>>> db.session.add(drink)                                                                       
>>> db.session.commit()                                                                         
>>> Drink.query.all()                                                                           
[Grape Soda - Tastes like grapes]                                                               
>>> db.session.add(Drink(name="Cherr", description="Taste like that one ice create"))           
>>> db.session.commit()                                                                         
>>> Drink.query.all()                                                                           
[Grape Soda - Tastes like grapes, Cherr - Taste like that one ice create]                       
>>>                                                                                             
