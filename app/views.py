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


# index  view function suppressed for brevity
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # validate_on_submit, 做了所有表单处理工作.在表单提交请求中被调用，它将会收集所有的数据，对字段进行验证，如果所有的事情都通过的话，它
    # 将会返回 True，表示数据都是合法的。
    if form.validate_on_submit():
        # flash 函数是一种快速的方式下呈现给用户的页面上显示一个消息。
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS']
                           )


# 两个 route 装饰器创建了从网址 / 以及 /index 到这个函数的映射
@app.route('/')
@app.route('/index')
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
