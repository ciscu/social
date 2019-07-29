from flask import render_template, flash, redirect
from app import app
from app.forms import loginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        flash('login requested for user {} and remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
