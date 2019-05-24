import datetime as dt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///tickets.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Station = Base.classes.station
Measurements = Base.classes.measurements

session = Session(engine)

app = Flask(__name__)

@app.route("https://api.seatgeek.com/2/events?")
def event():
    """Return a list of events"""
    return (
        f"venues available:"
    )


