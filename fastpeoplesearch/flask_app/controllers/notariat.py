from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request
from flask_app.models import Selenium_searching_notariat


@app.route('/notariat', methods=['POST'])
def notariat():
    return render_template('notariat.html')


@app.route('/notariat_get', methods=['POST'])
def notariat_get():
    fio = request.form['search']
    notariat_ex = Selenium_searching_notariat()
    result = notariat_ex.selenium_site_options(fio)
    return render_template('notariat_get.html', result=result)

