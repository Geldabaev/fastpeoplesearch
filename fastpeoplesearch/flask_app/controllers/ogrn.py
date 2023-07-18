from server import app
from flask import render_template
from flask_app.models import ogrn_func


@app.route('/ogrn', methods=['POST'])
def ogrn():
    res = ogrn_func()
    return render_template("ogrn.html", result=res)