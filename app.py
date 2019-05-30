import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import or_

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/data.sqlite"
db = SQLAlchemy(app)

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Games = Base.classes.games
Pricing = Base.classes.pricing
Venues = Base.classes.venues

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/teams")
def teams():
    teams = db.session.query(Games.team1).distinct()

    # Return a list of the column names (team names)
    return jsonify(list(teams))

@app.route("/games/<team>")
def game(team):
    sel = [
        Games.title,
        Venues.lat,
        Venues.lon,
    ]

    table = db.session.query(*sel).\
        join(Venues, Games.venue_id == Venues.venue_id).\
        filter(or_(Games.team1 == team, Games.team2 == team)).all()

    event_list = []
    for results in table:
        events = {}
        events["Event"] = results[0]
        events["Latitude"] = results[1]
        events["Longitude"] = results[2]
        event_list.append(events)

    return jsonify(event_list)

@app.route("/prices/<team>")
def price(team):
    sel = [
        Games.title,
        Pricing.low_price,
        Pricing.med_price,
        Pricing.high_price,
    ]

    table = db.session.query(*sel).\
        join(Pricing, Games.game_id == Pricing.game_id).\
        filter(or_(Games.team1 == team, Games.team2 == team)).all()

    event_pricing = []
    for results in table:
        events = {}
        events["Event"] = results[0]
        events["Low_price"] = results[1]
        events["Med_price"] = results[2]
        events["High_price"] = results[3]
        event_pricing.append(events)

    return jsonify(event_pricing)

@app.route("/map")
def map():
    """Return the map."""
    return render_template("map.html")

if __name__ == '__main__':
    app.run(debug=True)

