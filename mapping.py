from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from geopy.geocoders import Nominatim
import certifi
<<<<<<< HEAD
=======
import xml.etree.cElementTree as ET
>>>>>>> had to make some changes because I froze a folder

import urllib
from urllib.parse import urlparse

import psycopg2
import os
<<<<<<< HEAD



=======
import requests


# Configuring the app
>>>>>>> had to make some changes because I froze a folder
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ["MAPPING_SECRET_KEY"]

<<<<<<< HEAD
# Database setup
# url = urlparse(os.environ["DATABASE_URL"])
#
# database_connection = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

def uo(args, **kwargs):
	return urllib.request.urlopen(args, cafile=certifi.where(), **kwargs)

=======

# Creating a function to handle my geocoder errors
def uo(args, **kwargs):
	return urllib.request.urlopen(args, cafile=certifi.where(), **kwargs)

# Creating a reusable form class for my route inputs
>>>>>>> had to make some changes because I froze a folder
class InputForm(Form):
	start_address = TextField('Start Address:', validators=[validators.required()])
	destination_address = TextField('Destination Address:', validators=[validators.required()])

<<<<<<< HEAD
=======
# Creating the main endpoint for the app
>>>>>>> had to make some changes because I froze a folder
@app.route('/', methods=['GET', 'POST'])
def index():
	form = InputForm(request.form)
	if request.method == 'GET':
		return render_template('index.html', lat=40.703312, lng=-73.97968, form=form)

	if request.method == 'POST':
<<<<<<< HEAD
=======
		#  Handling the start and destination address
>>>>>>> had to make some changes because I froze a folder
		start_address = request.form['start_address']
		destination = request.form['destination_address']
		geolocator = Nominatim()
		geolocator.urlopen = uo
<<<<<<< HEAD
		start_location = geolocator.geocode(start_address)
		start_lat = start_location.latitude
		start_lng = start_location.longitude

		dest_location = geolocator.geocode(destination)
		destination_lat = dest_location.latitude
		destination_lng = dest_location.longitude
		return render_template('index.html',
								lat=start_lat, lng=start_lng,
								start_lat=start_lat, start_lng=start_lng,
								destination_lat=destination_lat,
								destination_lng=destination_lng,
								form=form)
=======
		try:
			start_location = geolocator.geocode(start_address)
			start_lat = start_location.latitude
			start_lng = start_location.longitude

			dest_location = geolocator.geocode(destination)
			destination_lat = dest_location.latitude
			destination_lng = dest_location.longitude

			return render_template('index.html',
									lat=start_lat, lng=start_lng,
									start_lat=start_lat, start_lng=start_lng,
									destination_lat=destination_lat,
									destination_lng=destination_lng,
									form=form)
		except:
			errors = "At least one of the addresses you entered is invalid. Please try again."
			return render_template('index.html', lat=40.703312, lng=-73.97968, form=form, errors=errors)


>>>>>>> had to make some changes because I froze a folder

if __name__ == '__main__':
	app.run(debug=True)
