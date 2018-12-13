from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'TurnDownForWhat'

@app.route('/')
def index():
    if 'name' not in session:
        session['name'] = ''
    if 'email' not in session:
        session['email'] = ''
    if 'comment' not in session:
        session['comment'] = ''
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['location'] = request.form['location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    if len(session['name']) < 1:
        flash('Name cannot be blank!', 'name')
    if len(session['email']) < 1:
        flash('Email cannot be blank!', 'email')
    if len(session['comment']) < 1:
        flash('Comment is required!', 'comment')
    elif len(session['comment']) > 120:
        flash('Comment cannot be longer than 120 characters!', 'comment')
    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/submitted')

@app.route('/submitted')
def submitted():
    return render_template('submitted.html')
@app.route('/danger')
def danger():
    print('A user tried to visit /danger')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)