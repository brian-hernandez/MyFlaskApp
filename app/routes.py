from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Brian'}
    posts = [
        {
            'author' : {'username' : 'Brian'},
            'body' : 'I am living in Cupertino for the Summer.',
            'times' : [0, 1, 2, 3, 4, 5, 6, 7]
        },
        {
            'author': {'username': 'Rascal'},
            'body': 'My favorite activity is going the park.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)