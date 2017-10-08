from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from urllib.parse import urlparse

import psycopg2
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ["MAPPING_SECRET_KEY"]

@app.route('/')
def index():
	return render_template('index.html')
#
# @app.route('/<lat>/<lng>')
# def custom(lat, lng):
#     return render_template('index.html', lat=lat, lng=lng)

if __name__ == '__main__':
	app.run(debug=False)
