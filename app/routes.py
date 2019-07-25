from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cis Cuypers'}
    posts = [
        {
            'author': {'username': 'Laure'},
            'body': 'Beautiful day in Retie!'
        },
        {
            'author': {'username': 'Cis'},
            'body': 'How to handle the heat'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
