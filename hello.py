from flask import Flask
from flask import render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)
@app.route('/')
def hello():
    return 'this is Flask object'

@app.route('/user/<user_name>')
def user(user_name):
    return '<h1>Welcome %s</h1>'%user_name
if __name__ == '__main__':
    manager.run()