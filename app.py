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

import mysql.connector

mydb = mysql.connector.connect(
 host="127.0.0.1",
 user="root",
 passwd="root",
 database="nfl_project"
)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/data.sqlite"
# db = SQLAlchemy(app)

# # Reflect an existing database into a new model
# Base = automap_base()

# # Reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# Games = Base.classes.games
# Pricing = Base.classes.pricing
# Venues = Base.classes.venues

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/teams")
def teams():
   """Return the team list."""
   mycursor = mydb.cursor()
   mycursor.execute("SELECT team1 FROM nfl_project.games GROUP BY team1;")
   myresult = mycursor.fetchall()
   team_list=[]
   for teams in myresult:
       team_list.append(teams)
   return(jsonify(team_list))

@app.route("/games/<team>")
def game(team):
    team_choice = team
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT title, lat, lon from games join venues on games.venue_id=venues.venue_id where team1='{team_choice}' or team2='{team_choice}' order by utcdate;")
    myresult = mycursor.fetchall()
    game_list=[]
    for teams in myresult:
        game_list.append(teams)
    return(jsonify(game_list))

@app.route("/map")
def map():
    """Return the map."""
    return render_template("map.html")

if __name__ == '__main__':
    app.run(debug=True)

