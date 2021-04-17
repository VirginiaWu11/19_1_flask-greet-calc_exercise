from flask import Flask
app=Flask(__name__)

# @app.route('/<greeting>/<place>')
# def greet(greeting,place):
    # return f"{greeting} {place}"

@app.route('/welcome')
def welcome():
    return 'welcome'
@app.route('/welcome/home')
def welcomeback():
    return 'welcome home'
@app.route('/welcome/back')
def welcomehome():
    return 'welcome back'
