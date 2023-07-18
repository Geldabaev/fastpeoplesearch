from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request, session
from flask_app.models import get_inn_info, Correction


@app.route('/inn', methods=['GET'])
def inn():
    return render_template('inn.html')


@app.route('/getinn', methods=['POST'])
def get_inn():
    last = request.form['last']
    first = request.form['first']
    surname = request.form['surname']
    date = Correction.correct_date(request.form['date'])
    docnumber = Correction.correct_docnumber(request.form['docnumber'])
    docdate = request.form['docdate']
    inn = get_inn_info()
    resinn = inn.main(last, first, surname, date, docnumber, docdate)
    resname = first + " " + last + " " + surname
    return render_template('get_inn.html', name=resname, inn=resinn['inn'])



