# !flask/bin/python
# -*- coding: utf8 -*-

import os
CSRF_ENABLED = True  # CSRF_ENABLED 配置是为了激活跨站点请求伪造保护
SECRET_KEY = 'you-will-never-guess'  # SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))
# 数据库文件路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# 把 SQLAlchemy-migrate 数据文件存储在这里
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
