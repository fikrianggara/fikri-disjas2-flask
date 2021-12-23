# app.py

# Required imports
# import os
from flask import Flask, request, jsonify
from pyflightdata import FlightData
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)
flightData = FlightData()
# airport = 'WAAA'


@app.route("/")
def hello():
    return "<h1>Selamat Meng-Disjas Gaess!</h1>"


@app.route('/<airport>/details/<page>', methods=['GET'])
def airportDetailss(airport, page):
    data = flightData.get_airport_details(airport, page=page)
    return jsonify(data), 200


@app.route('/<airport>/arrivals/<page>', methods=['GET'])
def airportArrivals(airport, page):
    data = flightData.get_airport_arrivals(iata=airport, page=page, earlier_data=True)
    return jsonify(data), 200


@app.route('/<airport>/departures/<page>', methods=['GET'])
def airportDepartures(airport, page):
    data = flightData.get_airport_departures(airport, page=page, earlier_data=True)
    return jsonify(data), 200


@app.route('/<airport>/onground/<page>', methods=['GET'])
def airportOnground(airport, page):
    data = flightData.get_airport_onground(airport, page=page)
    return jsonify(data), 200


@app.route('/<airport>/weather/<page>', methods=['GET'])
def airportWeather(airport, page):
    data = flightData.get_airport_weather(airport, page=page)
    return jsonify(data), 200


@app.route('/<airport>/stat/<page>', methods=['GET'])
def airportStat(airport, page):
    data = flightData.get_airport_stats(airport, page=page)
    return jsonify(data), 200
