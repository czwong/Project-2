# Project-2
It project 2 time
-------------------------------------------------------------------------------------------------------------------------------------------
Your task is to tell a story through data visualizations.
Focus on providing users an interactive means to explore data themselves.
Prepare a 10-minute presentation that lays out your theme, coding approach, data munging techniques, and final visualization.
You may choose a project of any theme, but we encourage you to think broadly.
You will have ample time in class to work with your group, but expect to put in hours outside of class as well.


## Specific Requirements
1. Your visualization must include a Python Flask–powered RESTful API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.).
2. Your project should fall into one of the below four tracks:
- A custom "creative" D3.js project (i.e., a nonstandard graph or chart)
- A combination of web scraping and Leaflet or Plotly
- A dashboard page with multiple charts that update from the same data
- A "thick" server that performs multiple manipulations on data in a database prior to visualization (must be approved)
3. Your project should include at least one JS library that we did not cover.
4. Your project must be powered by a data set with at least 100 records.
5. Your project must include some level of user-driven interaction (e.g., menus, dropdowns, textboxes).
6. Your final visualization should ideally include at least three views.

-------------------------------------------------------------------------------------------------------------------------------------------
Ticketmaster api 
https://developer.ticketmaster.com/products-and-docs/apis/getting-started/
-------------------------------------------------------------------------------------------------------------------------------------------

Data Source:* Ticketmaster Developer API
Database:* MongoDB
Project Category:* A combination of web scraping and Leaflet or Plotly
JS Library We Haven't Used:* JQuerey
Data Set With 100+ Records:* We will pull data for at least 100 events.
User Interaction:* The event map will have toggles based on the event category.
Three Visualization Views:* Event map and two charts that analyze price/popularity
-------------------------------------------------------------------------------------------------------------------------------------------
Content Repo
- [db folder]
- [static folder]
- [templates]
- [.gitignore]
- [Procfile](Procfile)
- [__init__.py](__init__.py)
- [app.py](app.py)
- [requirements.txt](requirements.txt)
----------------------------------------------------------------------------------------------------------------------------------------
Before Starting 
create an API key using this link https://developer.ticketmaster.com/products-and-docs/apis/getting-started/ .
Once you have your API key go to static/map_js/config.js and place your  API_KEY, client_id, and client_secret.
You will need to install some module if you do not have them before running the app.py. In the requirements you'll see what you will need and the version of the module.

----------------------------------------------------------------------------------------------------------------------------------------
Procedures
Step 1:
- Make sure that you have updated the config.js file
- Run nfl_etl.py in the db folder
Step 2:
From the project folder, run:
$ python app.py
- once you run the app copy and paste "http://127.0.0.1:5000/" from your terminal and pasted it into your browser.




