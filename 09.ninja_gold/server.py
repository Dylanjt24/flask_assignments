from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)