from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
#flask --app HelloFlask.py --debug run

app = Flask(__name__) #name of file
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return 'Hello word from Flask!'

@app.route('/sweet')
def sweet():
    return '<h1>Sweet</h1><br>candies'

@app.route('/template')
def t_test():
    return render_template('index.html')