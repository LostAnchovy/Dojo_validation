from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'not a very secret key'

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/register", methods=['POST'])
def submit():
  form_valid =True
  if len(request.form['name']) == 0: 
    flash("Please fill in your name!!")
    form_valid = False
  elif not (request.form['name']).isalpha():
  # name must NOT be numbers. Must be characters.
  # The method isalpha() checks whether the string consists of alphabetic characters only.
    flash('please enter a name')
    form_valid = False 

  if len(request.form['location'])<0:
    flash('please pick a location')
    form_valid = False

  if len(request.form['language'])<0:
    flash('please pick a language')
    form_valid = False

  if len(request.form['comment'])>120:
    flash('comments are limited to 120 characters')
    form_valid = False

  if form_valid:
    flash("Sucess!! Thank you for registering {}".format(request.form['name']))
  return redirect('/')
app.run(debug=True)