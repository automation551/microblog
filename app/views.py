# !flask/bin/python
# -*- coding: utf8 -*-
"""
Created on 16/5/24

@author: wb-lanxiang

function:
    
"""
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
# index  view function suppressed for brevity
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS']
                           )


@app.route('/index')
# 两个 route 装饰器创建了从网址 / 以及 /index 到这个函数的映射
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
