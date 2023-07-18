from server import app
from flask_app.config import connectToMySQL
from flask import render_template, redirect, request
# from blackbird import blackbird


@app.route('/network', methods=['POST'])
def network():
    return redirect("http://127.0.0.1:9797/")  # blackbird
