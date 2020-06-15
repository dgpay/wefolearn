from flask import Flask, request, session, redirect, url_for, render_template, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DATABASE.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=1)
db = SQLAlchemy(app)

if __name__ == "__main__":
    
    # We need to make sure Flask knows about its views before we run
    # the app, so we import them. We could do it earlier, but there's
    # a risk that we may run into circular dependencies, so we do it at the
    # last minute here.

    from routing import *

    app.run(debug=True)