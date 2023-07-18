from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request
from flask_app.models import Selenium_searching


@app.route('/federal', methods=['POST'])
def federal():
    return render_template("federal.html")


@app.route('/resfederal', methods=['POST'])
def resfederal():
    s_family = request.form['last']
    fio = request.form['first']
    d_year = request.form['year']
    mail = request.form['mail']
    federal = Selenium_searching(s_family, fio, d_year, mail)
    result = federal.selenium_site_options()
    return render_template("resfederal.html", result=result)
