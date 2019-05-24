#Import Dependencies
import requests
import json
from pprint import pprint

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root",
  database="nfl_project"
)
mycursor = mydb.cursor()

#Define API URL and Key
base = "https://api.seatgeek.com/2/events?"
key="MTY2Njc1Njd8MTU1ODA1NzIyNy44OQ"
start_date="2019-09-05"
sport="nfl"

#Build API String
string=f"{base}&client_id={key}&datetime_utc.gte={start_date}&type={sport}&per_page=1"
data=requests.get(string).json()

#Venue Data
venue_id=data["events"][0]["venue"]["id"]
lat=data["events"][0]["venue"]["location"]["lat"]
lon=data["events"][0]["venue"]["location"]["lon"]

venue_data=(venue_id,lat,lon)
venueInsert = "INSERT INTO venues (venue_id, lat, lon) VALUES (%s, %s, %s)"
mycursor.execute(venueInsert, venue_id)

