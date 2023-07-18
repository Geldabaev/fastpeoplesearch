from server import app
from flask import render_template, redirect, request
from flask_app.models import ScheduleDownloadFile, Analise


@app.route('/pasport', methods=['POST'])
def posport():
    return render_template('pasport.html')


@app.route('/analisepasport', methods=['POST'])
def analisepasport():
    series = request.form['series']
    number = request.form['number']
    print("Ждите...")
    analise_result = Analise().filter_data(series, number)

    return render_template('analisepasport.html', analise_result=analise_result)


@app.route('/action_pasport', methods=['POST'])
def action_pasport():
    return render_template('action_pasport.html')