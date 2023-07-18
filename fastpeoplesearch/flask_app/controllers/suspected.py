from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request
from flask_app.models import Suspected


@app.route('/suspected', methods=['POST'])
def suspected():
    return render_template('suspected.html')


@app.route('/ressuspected', methods=['POST'])
def ressuspected():
    sus = request.form['search']
    suspect = Suspected()
    res_sus = suspect.selenium_site_options(sus)
    return render_template('ressuspected.html', res_sus=res_sus)
