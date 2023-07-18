from flask_app import app
from flask_app.controllers import (other, inn, ogrn, pasport, criminal,
                                   federal, interpol, suspected, no_trust,
                                   notariat, fet_not_pal, network)
from flask import render_template
from flask import Flask


if __name__ == '__main__':
    app.run(debug=True)
