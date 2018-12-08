from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def submitted():
    return render_template('submitted.html')

@app.route('/danger')
def danger():
    print('A user tried to visit /danger')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)