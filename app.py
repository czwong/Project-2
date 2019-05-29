import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

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
# Games = Base.classes.games
# Pricing = Base.classes.pricing
# Venues = Base.classes.venues

@app.route("/map")
def map():
    """Return the map."""
    return render_template("Map/map.html")

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

# @app.route("/games")
# def names():
#     """Return a list of sample names."""

#     # Use Pandas to perform the sql query
#     games = db.session.query(Games).all()
#     df = pd.read_sql_query(games, db.session.bind)

#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns))

if __name__ == '__main__':
    app.run(debug=True)

