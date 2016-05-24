# !flask/bin/python
# -*- coding: utf8 -*-
"""
Created on 16/5/24

@author: wb-lanxiang

function:
    
"""
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

