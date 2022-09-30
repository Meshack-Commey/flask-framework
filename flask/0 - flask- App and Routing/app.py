from flask import Flask, redirect, url_for, request, render_template
from flask import *
app = Flask(__name__)
#Secret Key of the application
app.secret_key = 'meshcom'

#flask URL BUILDING using url_for() with redirect object
app.route('/admin') #admin
def admin():
    return 'hello admin'

@app.route('/guest/<guest>')
def guest(guest):
    return f'Welcome {guest}, your are a guest'

@app.route('/user/<name>')
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))

#############################################################
##flask HTTP Methods for HTML Login FORM
###
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        firstName = request.form['fname']
        lastName = request.form['lname']
        return f'Post: {firstName} {lastName}'
    else:
        firstName = request.args.get('fname')
        lastName = request.args.get('lname')
        return f'Get: {firstName} {lastName}'

###############################################################
##flask  TEMPLATES
###
@app.route('/index/<int:score>')
def index(score):
    return render_template('index.html', mark=score)

@app.route('/result')
def result():
    dic = {'phy':50, 'che':60, 'maths':70}
    return render_template('result.html', result=dic)

##############################################################
##flask STATIC FILES
###
@app.route('/jsfile')
def jsfile():
    return render_template('js.html')

##############################################################
##flask SENDING FORM DATA TO TEMPLATE
###
@app.route('/exams_record')
def exams_record():
    return render_template('exams_record.html')

@app.route('/exams_result', methods = ['POST', 'GET'])
def exams_result():
    if request.method == 'POST':
        show_result = request.form
        return render_template('exams_result.html', result=show_result)

########################################################################
##flask COOKIES : A COOKIE is stored on a client's computer in 
# the form of a text file It's purpose is to remember and track 
# data pertaining to client's usage for better visitor experience
#  and site statistics
###
#A simple form that gets user ID
#the form will be posted to "/setcookie" URL
@app.route('/cookie_index')
def cookie_index():
    return render_template('cookie_index.html')

#This view function sets a Cookie name 'userID' 
# and renders another page 'readcookie.html' which contains a hyperlink 
# to another view function '/getcookie'
@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        #get a request from html FORM
        user = request.form['userID']
        #send the response to 'readcookie.html'
        make = make_response(render_template('readcookie.html'))
        #set cookie after a response is made
        make.set_cookie('userID', user)
        return make

#this view function reads back and displays the cookie value in 
#browser when the link in 'readcookie.html' is clicked
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

###############################################################
##flask SESSIONS : Unlike a Cookie, Session data is stored on server.
#Session is the time interval when a client logs into a server and 
#logs out of it. The data, which is needed to be held across this session, 
# is stored in a temporary directory on the server. 
#Ensure to set secret_key of the application
##############################################
#URL '/logindex' shows the opening page which simply prompts user to log in, 
# as session variable 'username' is not set
@app.route('/logindex')
def logindex():
    if 'username' in session:
        username = session['username']
        return 'Logged in as '+username+'<br><br>'+'<a href="http://localhost:5000/logout">click here to logout</a>'
    return "You are not logged in <br><br>"+"<a href='http://localhost:5000/log_in'>Click here to login</a>"

#log_in() view function opens up a login form.
#The form is posted back to URL '/log_in' and now session variable is set.
#Application is redirected to '/logindex' since session variable is found.
@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('logindex'))
    return '''
    <form action="http://localhost:5000/log_in" method="POST">
        <p><input type="text" name="username" placeholder="Enter username"></p>
        <p><input type="submit" value="submit"></p>
    </form>
    '''

#logout() view function which pops put 'username' session variable.
#Hence, '/logindex' URL again shows the opening page.
#session.pop() is used to release a session variable i.e. 
@app.route('/logout')
def logout():
    #remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('logindex'))




if __name__ == '__main__':
    app.run(debug=True)