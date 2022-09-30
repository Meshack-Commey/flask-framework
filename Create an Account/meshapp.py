from flask import Flask, render_template, url_for, redirect, flash,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MeshCom@localhost:5432/meshapps'
app.config['SECRET_KEY'] = 'mesh strings'

db = SQLAlchemy(app)

#User Model
class users(db.Model):
    __tablename__ = 'user'
    id = db.Column('user_id', db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(30))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, firstname, lastname, username, email, password):
        self.firstname = firstname,
        self.lastname = lastname,
        self.username = username,
        self.email = email,
        self.password = password
     
#Routes & Views
@app.route('/main')
def main():
    return render_template('layouts/main.html')

@app.route('/signpage')
def signpage():
    if request.method == 'POST':
        if not request.form['firstname'] or not request.form['lastname'] or not request.form['username'] or not request.form['email'] or not request.form['password']:
            flash('please, fill all fields', 'error')
        else:
            user = users(request.form['firstname'], request.form['lastname'], request.form['username'], request.form['email'], request.form['password'])
            db.session.add(user)
            db.session.commit()
            flash('User added successfully')
            return redirect(url_for('main'))
    return render_template('pages/signpage.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)