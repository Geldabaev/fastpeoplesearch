from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request
from flask_app.models import search_in_sqlite3


@app.route('/no_trust', methods=['POST'])
def no_trust_start():
    return render_template('no_trust.html')

# Белокрылова Алла Марковна
@app.route('/get_trust', methods=['POST'])
def get_trust():
    result = request.form['search'].split(' ')
    res = search_in_sqlite3(result)
    print(res)
    return render_template('get_trust.html', res=res)