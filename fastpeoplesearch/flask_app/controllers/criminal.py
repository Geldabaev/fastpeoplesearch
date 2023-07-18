from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request
from flask_app.models import criminal_info


@app.route('/criminal', methods=['POST'])
def criminal():
    return render_template("criminal_input.html")


@app.route('/criminal/result', methods=['POST'])
def criminal_result():
    criminal_res = request.form['fio']
    criminals = criminal_info(criminal_res)
    return render_template("criminal_result.html", criminals=criminals)