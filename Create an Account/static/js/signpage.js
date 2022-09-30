//sign up to your account
function signUp(){
   var signup = "<form class='account' action='{{ url_for('signpage') }}' method='post'><h1>Create your account</h1><br/><p>Build skills for today, tomorrow and beyound.</p><br><br><input type='text' name='firstname' placeholder='First Name'><br><br><input type='text' name='lastname' placeholder='Last Name'><br><br><input type='text' name='username' placeholder='username'><br><br><input type='email' name='email' placeholder='Email'><br><br><input type='password' name='password' placeholder='Password'><br><br><input type='submit'><br></form>";
   var Signup = document.getElementById('signed').innerHTML=signup;
   return Signup;
    }
  
//sign in to your account
const signIn = function() {
   var signin = "<form class='account' action='request.path' method='post'><h1>Sign in to your account</h1><br><input type='email' name='email' placeholder='Email'><br><br><input type='password' name='password' placeholder='Password'><br><br><input type='submit'><br></form>";
   var sign_in = document.getElementById('signed')
   var Signin = sign_in.innerHTML=signin;
   return Signin;
  }

//single-sign-on (SSO) Authentication Method
let gmail = document.getSelector('#gmail')
let facebook = document.getSelector('#facebook')

const signOn = (gmail, facebook) => {
  this.gmail = gmail.innerHTML="link to gmail signon page",
  this.facebook = facebook.innerHTML="link to facebook signon page"
}