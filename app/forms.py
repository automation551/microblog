# !flask/bin/python
# -*- coding: utf8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    # BooleanField一个CheckboxInput对象
    remember_me = BooleanField('remember_me', default=False)
