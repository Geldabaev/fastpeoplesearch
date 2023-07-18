from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request, session


@app.route('/')
def index():
    return render_template('index.html')
