from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brian'}
    posts = [
        {
            'author': {'username': 'Brian'},
            'body': 'I am living in Cupertino for the Summer.'
        },
        {
            'author': {'username': 'Rascal'},
            'body': 'My favorite activity is going the park.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
