from flask import Flask, render_template, redirect,url_for, request, flash
from flask_sqlalchemy import SQLAlchemy 

#flask application configuration
app = Flask(__name__)
#set URI for the database to be use
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MeshCom@localhost:5432/schoolbase'
app.config['SECRET_KEY'] = 'random string'
#Instance of SQLAlchemy class
db = SQLAlchemy(app)

#students model
class students(db.Model):
    id = db.Column('student_id', db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    address = db.Column(db.String(100))
    pin = db.Column(db.String(100))
    #class constractor
    def __init__(self, name, city, address, pin):
        self.name = name,
        self.city = city,
        self.address = address,
        self.pin = pin

#entry point of the application is show_all() bound to '/' URL
@app.route('/')
def show_all():
    return render_template('show_all.html') #render 'show_all.hmtl' as homepage

@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['address'] or not request.form['pin']:
            flash('Please enter all the fields', 'error') #message flashing
        else:
            student = students(request.form['name'], request.form['city'], request.form['address'], request.form['pin'])
            db.session.add(student) #inserts the form data into the database
            db.session.commit() #commit changes
            flash('Record was successfully added')
            return redirect(url_for('show_all')) #redirects to show all data inserted student data
    return render_template('new.html') #render 'new.html' page to add students





if __name__ == '__main__':
    db.create_all() #to create or use database mentioned in URI, run the create_all() method
    app.run(debug=True)



