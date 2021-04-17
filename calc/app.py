# Put your app in here.
from flask import Flask, request
app= Flask(__name__)

from operations import *

@app.route('/add')
def ad():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a,b))
@app.route('/sub')
def su():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a,b))
@app.route('/mult')
def mu():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))
@app.route('/div')
def di():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))



@app.route('/math/<oper>')
def oper(oper):
    operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
    a = int(request.args['a'])
    b = int(request.args['b'])
    print(oper)
    return str(operators[oper](a,b))
