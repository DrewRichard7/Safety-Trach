from flask import Flask, render_template
app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


if __name__ == '__main__':
    app.run(debug=1, host='0.0.0.0')
# *1. -> notes.txt
