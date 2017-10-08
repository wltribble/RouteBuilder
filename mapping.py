from flask import Flask, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, SubmitField
from geopy.geocoders import Nominatim
import certifi

import urllib
import os



# Configuring the app

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ["MAPPING_SECRET_KEY"]


# Creating a function to handle my geocoder errors
def uo(args, **kwargs):
	return urllib.request.urlopen(args, cafile=certifi.where(), **kwargs)

# Creating a reusable form class for my route inputs

class InputForm(Form):
	start_address = TextField('Start Address:', validators=[validators.required()])
	destination_address = TextField('Destination Address:', validators=[validators.required()])

# Creating the main endpoint for the app
@app.route('/', methods=['GET', 'POST'])
def index():
	form = InputForm(request.form)
	if request.method == 'GET':
		return render_template('index.html', lat=40.703312, lng=-73.97968, form=form)

	if request.method == 'POST':
		#  Handling the start and destination address
		try:
			start_address = request.form['start_address']
			destination = request.form['destination_address']
			geolocator = Nominatim()
			geolocator.urlopen = uo
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



if __name__ == '__main__':
	app.run(debug=True)
