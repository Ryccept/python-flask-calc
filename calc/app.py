# Put your app in here.

from flask import Flask, request

from operations import *

app = Flask(__name__)

@app.route('/add')
def add_page():
    a = request.args['a']
    b = request.args['b']
    answer = int(a)+int(b)
    return f'{answer}'

@app.route('/sub')
def sub_page():
    a = request.args['a']
    b = request.args['b']
    answer = int(a)-int(b)
    return f'{answer}'


@app.route('/mult')
def mult_page():
    a = request.args['a']
    b = request.args['b']
    answer = int(a)*int(b)
    return f'{answer}'


@app.route('/div')
def div_page():
    a = request.args['a']
    b = request.args['b']
    answer = int(a)/int(b)
    return f'{answer}'