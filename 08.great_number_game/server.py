from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'randomNum' not in session:
        session['randomNum'] = random.randrange(1,101)
        print(session['randomNum'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['number'])
    if guess > session['randomNum']:
        session['message'] = "Too high"
    elif guess < session['randomNum']:
        session['message'] = "Too low"
    else:
        session['message'] = "Correct"
    return redirect('/')

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)