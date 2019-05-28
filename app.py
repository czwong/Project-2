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
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('file:///C:/Users/jgome/Desktop/Project-2/landing.html')

if __name__ == '__main__':
    app.run()
