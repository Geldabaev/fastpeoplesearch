from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request
from flask_app.models import interpol_mod


@app.route('/interpol', methods=['POST'])
def interpol():
    return render_template('interpol.html')


@app.route('/resinterpol', methods=['POST'])
def resinterpol():
    name = request.form['name']
    forename = request.form['forename']
    print(name, forename)
    results = interpol_mod(name, forename)
    return render_template('resinterpol.html', results=results)