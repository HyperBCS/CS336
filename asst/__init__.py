from flask import Flask, render_template, flash
from peewee import MySQLDatabase, fn
import sys, traceback
import flask_login


def init_db():
    global DB
    DB = MySQLDatabase(host="ofmc.me",port=3306,user="cs336",passwd="password",database="cs336")


APP = Flask(__name__, template_folder="views/templates", static_url_path='/static')
APP.secret_key = 'A^*4L#Cs8UjQaq!Hjmhz'

LM = flask_login.LoginManager()
LM.init_app(APP)

init_db()

import asst.auth

# Register all views after here
# =======================
from asst.auth import auth_pages
from asst.views import register


APP.register_blueprint(register.page, url_prefix='/register')
APP.register_blueprint(auth_pages, url_prefix='/auth')

# ==================================== Universal Routes ======================================== #
@APP.route('/')
def index():
    ''''Renders the default template'''
    if flask_login.current_user.is_authenticated:
        return render_template('index.html',
                               message='Hello {}'.format(flask_login.current_user.Name),
                               logged_in=True,
                               role=flask_login.current_user.role)
    else:
        return render_template('index.html',logged_in=False)

# =============================================================================================== #