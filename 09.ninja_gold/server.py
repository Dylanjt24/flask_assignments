from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    today = str(datetime.now().strftime("%Y/%m/%d %I:%M %p"))
    if request.form['building'] == 'farm':
        winnings = random.randrange(10,21)
        session['gold'] += winnings
        session['activities'].append('<p style="color: green;">' +'Earned ' + str(winnings) + ' gold from the farm!' + ' (' + today + ')' + '</p>')
    elif request.form['building'] == 'cave':
        winnings = random.randrange(5,11)
        session['gold'] += winnings
        session['activities'].append('<p style="color: green;">' +'Earned ' + str(winnings) + ' gold from the cave!' + ' (' + today + ')' + '</p>')
    elif request.form['building'] == 'house':
        winnings = random.randrange(2,6)
        session['gold'] += winnings
        session['activities'].append('<p style="color: green;">' +'Earned ' + str(winnings) + ' gold from the house!' + ' (' + today + ')' + '</p>')
    elif request.form['building'] == 'casino':
        winnings = random.randrange(-50,51)
        session['gold'] += winnings
        if winnings >= 0:
            session['activities'].append('<p style="color: green;">' +'Earned ' + str(winnings) + ' gold from the casino!' + ' (' + today + ')' + '</p>')
        else:
            session['activities'].append('<p style="color: red;">' +'Entered a casino and lost ' + str(winnings) + ' gold... Ouch... (' + today + ')' + '</p>')
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)