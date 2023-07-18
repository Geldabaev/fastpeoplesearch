from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request
from flask_app.models import FetNotPal


@app.route('/fet_not_pal', methods=['POST'])
def fet_not_pal():
    return render_template('fet_not_pal.html')


@app.route('/get_fet_not_pal', methods=['POST'])
def get_fet_not_pal():
    print(request.form['search'])
    not_pal = FetNotPal()
    res = not_pal.selenium_site_options(request.form['search'])
    return render_template('get_fet_not_pal.html', result=res)