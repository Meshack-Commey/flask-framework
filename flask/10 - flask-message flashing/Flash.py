#importing modules
from flask import Flask, render_template, request, redirect, url_for, flash
#initialize flask application
app = Flask(__name__)
app.secret_key = 'meshcom'

#index view function
@app.route('/')
def index():
    return render_template('index.html')

#login view function
@app.route('/login', methods = ['POST', 'GET'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error = error)


#run application
if __name__ == '__main__':
    app.run(debug=True)