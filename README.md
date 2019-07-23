# Project-2
-------------------------------------------------------------------------------------------------------------------------------------------
Ticketmaster api 
https://developer.ticketmaster.com/products-and-docs/apis/getting-started/
-------------------------------------------------------------------------------------------------------------------------------------------
Hello football fans, when it comes to tracking your favorite team it can get hectic. You go from page to page looking for when your team plays next. Isn't it exausting? well we made a page for you. When opening the page you'll see a dropdown menu clicking on the dropdown will show you a list of teams choose your favorite team and see the map come alive with you teams location, the price of tickets, and using the next game button will take you to the next game see if it is home or away. 
-------------------------------------------------------------------------------------------------------------------------------------------
### Content Repo
- [`db`](db) contains data.sqlite and nfl_elt.py
- [`static`](static) contains img, index_images, map_css, map_js, app.js, style.css
- [`templates`](templates) contains index.html and map.html
- [`app.py`](app.py)
- [`requirements.txt`](requirements.txt)
----------------------------------------------------------------------------------------------------------------------------------------
Before Starting 
create an API key using this link https://developer.ticketmaster.com/products-and-docs/apis/getting-started/ .
Once you have your API key go to static/map_js/config.js and place your  API_KEY, client_id, and client_secret.
You will need to install some module if you do not have them before running the app.py. In the requirements you'll see what you will need and the version of the module.

----------------------------------------------------------------------------------------------------------------------------------------
### Procedures
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

### Website/Herokuapp
https://nfl-data-game.herokuapp.com
