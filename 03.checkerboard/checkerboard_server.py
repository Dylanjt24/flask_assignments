from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<x>/<y>')
def x_by_y(x,y):
    return render_template('x_by_y.html', x=int(x), y=int(y))

if __name__=='__main__':
    app.run(debug=True)