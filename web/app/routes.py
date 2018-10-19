from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, DialogForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'I\'m SDS system!'}
    form = DialogForm()
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    if form.validate_on_submit():
        posts = [
            {
                'author': {'username': 'User'},
                'body': form.query.data
            }
        ]
        return render_template('index.html', title='Home', user=user, posts=posts, form=form)
    
    return render_template('index.html', title='Home', user=user, posts=posts, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
