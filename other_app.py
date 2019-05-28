# import datetime as dt
# import numpy as np
# import pandas as pd
# import datetime as dt
# import jsonify
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func

# engine = create_engine("sqlite:///nfl_sqlite")
# Base = automap_base()
# Base.prepare(engine, reflect=True)

# Station = Base.classes.Station
# Measurements = Base.classes.Measurements

# session = Session(engine)

# app = Flask(__name__)

# @app.route("https://api.seatgeek.com/2/events?")
# def welcome():
#     """api route"""
#     return jsonify()

# @app.route("file:///C:/Users/jgome/Desktop/Project-2/landing.html")
# def welcome():
#     return()

from flask import Flask

app = Flask(__name__)

from app import routes


app.run(debug=True)