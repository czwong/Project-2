# import datetime as dt
# import numpy as np
# import pandas as pd
# import datetime as dt
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
# from flask import Flask, jsonify

# engine = create_engine("sqlite:///tickets.sqlite")
# Base = automap_base()
# Base.prepare(engine, reflect=True)

# Station = Base.classes.station
# Measurements = Base.classes.measurements

# session = Session(engine)

# app = Flask(__name__)

# @app.route("https://api.seatgeek.com/2/events?")
# def event():
#     """Return a list of events"""
#     return (
#         f"venues available:"
#     )
import flask
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import sqlite3


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
        return d

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to the 'Home' page!"

datetime = []

@app.route('https://api.seatgeek.com/2/events?client_id=MTY2Njc1Njd8MTU1ODA1NzIyNy44OQ&datetime_utc.gte=2019-09-05&type=nfl&sort=datetime_utc.asc&per_page=300', methods=['GET'])
def api_datetime():
    return jsonify(datetime)

teams = []

@app.route('https://api.seatgeek.com/2/events?client_id=MTY2Njc1Njd8MTU1ODA1NzIyNy44OQ&datetime_utc.gte=2019-09-05&type=nfl&sort=datetime_utc.asc&per_page=300', methods=['GET'])
def api_teams():
    return jsonify(teams)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page Not Found.</p>", 404

@app.route('https://api.seatgeek.com/2/events?client_id=MTY2Njc1Njd8MTU1ODA1NzIyNy44OQ&datetime_utc.gte=2019-09-05&type=nfl&sort=datetime_utc.asc&per_page=300', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    title = query_parameters.get('title')
    lat = query_parameters.get('lat')
    lon = query_parameters.get('lon')
    venues = query_parameters.get('venues')
    pricing = query_parameters.get('pricing')

    query = "SELECT team1 FROM nfl_project.games"
    to_filter = []

    if id:
        query += 'id=? AND'
        to_filter.append(id)
    if not (id):
        return page_not_found(404)
    
query = query[:-4] + ';'

conn = sqlite3.connect('teams.db')
conn.row_factory = dict_factory
cur = conn.cursor()

results = cur.execute(query, to_filter).fetchall()

return jsonify(results)

if __name__ == '__main__':
    app.run()

