Project Structure

|- README.md
|- app.py   ***The main driver of the app includes SQLAlchemy models
|- config.py ***Database URIs, CSRF generation
|- error.log
|- forms.py ***Your forms
|- requirements.txt ***The dependancies we need to install with pip3 install -r requirements.txt

|- static
  |- css
  |- font
  |- ico
  |- img
  |- jss
|
|- templates
  |- errors
  |- forms
  |- layouts
  |- pages


*** MODEL - VIEW - CONTROLLER ***

|- Model
  |- CREATE DATABASE meshapps;
  |- CREATE TABLE users(
    id INT PRIMARY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    username VARCHAR(30),
    email VARCHAR(100),
    password VARCHAR(100)
  );

|- View

|- Controller