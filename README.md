# Project-2
It project 2 time
-------------------------------------------------------------------------------------------------------------------------------------------
Ticketmaster api 
https://developer.ticketmaster.com/products-and-docs/apis/getting-started/
-------------------------------------------------------------------------------------------------------------------------------------------

Data Source:* Ticketmaster Developer API
Database:* Mysqlite
Project Category:* A combination of web scraping and Leaflet or Plotly
JS Library We Haven't Used:* JQuery
Data Set With 100+ Records:* We will pull data for at least 100 events.
User Interaction:* The event map will have toggles based on the event category.
Three Visualization Views:* Event map and two charts that analyze price/popularity
-------------------------------------------------------------------------------------------------------------------------------------------
Content Repo
- [`db`](db) contains data.sqlite and nfl_elt.py
- [`static`](static) contains img, index_images, map_css, map_js, app.js, style.css
- [`templates`](templates) contains index.html and map.html
- [`Procfile`](Procfile)
- [`app.py`](app.py)
- [`requirements.txt`](requirements.txt)
----------------------------------------------------------------------------------------------------------------------------------------
Before Starting 
create an API key using this link https://developer.ticketmaster.com/products-and-docs/apis/getting-started/ .
Once you have your API key go to static/map_js/config.js and place your  API_KEY, client_id, and client_secret.
You will need to install some module if you do not have them before running the app.py. In the requirements you'll see what you will need and the version of the module.

----------------------------------------------------------------------------------------------------------------------------------------
Procedures
Step 1:
- Make sure that you have updated the config.js file
- Run
```
nfl_etl.py
``` 
in the db folder
Step 2:
From the project folder, run:
```
$ python app.py
```
- once you run the app copy and paste "http://127.0.0.1:5000/" from your terminal and pasted it into your browser.




