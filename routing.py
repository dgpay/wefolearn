from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify

from models import *


@app.route('/')
def showHome():
    return render_template('index.html')


@app.route('/register')
def showHome():
    return render_template('re.html')