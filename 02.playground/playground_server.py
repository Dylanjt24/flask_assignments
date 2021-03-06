from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html')

@app.route('/play/<num>')
def repeat(num):
    return render_template('repeat.html', num=int(num))

@app.route('/play/<num>/<color>')
def repeat_color(num,color):
    return render_template('repeat_color.html', num=int(num), color=color)

if __name__=='__main__':
    app.run(debug=True)