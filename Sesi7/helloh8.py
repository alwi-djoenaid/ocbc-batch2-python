from flask import Flask
from flask import request
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():    
    return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World!'

@app.route('/user/<username>')
def showUserProfile(username):
    return f'User {escape(username)}'

@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':        
        return do_the_login()    
    else:    
        return show_the_login_form()

def do_the_login():
    return 'Logged in'

def show_the_login_form():
    return 'Sign in first'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):    
    return render_template('hello.html', name=name)
    
if __name__ == '__main__':    
    app.run(debug=True)
