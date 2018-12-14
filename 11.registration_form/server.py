from flask import Flask, redirect, render_template, request, session, flash
import re
app = Flask(__name__)
app.secret_key = "WhoLetTheDogsOut"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

@app.route('/')
def index():
    # if 'first_name' not in session:
    #     session['first_name'] = ''
    # if 'last_name' not in session:
    #     session['last_name'] = ''
    # if 'email' not in session:
    #     session['email'] = ''
    
    return render_template('index.html')

@app.route('/submitted', methods=['POST'])
def submitted():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank!", "first_name")
    elif not session['first_name'].isalpha():
        flash("First name must only contain letters!", "first_name")
    if len(session['last_name']) < 1:
        flash("Last name cannot be blank!", "last_name")
    elif not session['last_name'].isalpha():
        flash("Last name must only contain letters!", "last_name")
    if not EMAIL_REGEX.match(session['email']):
        flash("Invalid email address!", "email")
    if len(request.form['password']) < 8:
        flash("Password must be more than 8 characters!", "password")
    elif request.form['password'] != request.form['confirm_password']:
        flash("Passwords must match!", "password")
    elif not PW_REGEX.match(request.form['password']):
        flash("Password must contain at least 1 uppercase letter and 1 number!", "password")

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/result')

@app.route('/result')
def result():
    session.clear()
    flash('Thanks for submitting your information!')
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)