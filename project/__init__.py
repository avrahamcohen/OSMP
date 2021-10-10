import os
import uuid
import secrets
import getpass
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from flask import Flask, g, request, session, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config['username'] = getpass.getuser()
app.config['SESSION_COOKIE_SECURE '] = True

csrf = CSRFProtect(app)

SELF = "'self'"
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': SELF,
        'img-src': [
            SELF,
            "'unsafe-inline'",
        ],
        'media-src': [
            SELF,
            "'unsafe-inline'"
        ],
        'script-src': SELF,
        'style-src': [
            SELF,
            "'unsafe-inline'"
        ]
    },
    content_security_policy_nonce_in=['script-src'],
    feature_policy={
        'geolocation': '\'none\'',
    }
)

csrf.init_app(app)

from project.controllers import *
