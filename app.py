import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root",
  database="nfl_project"
)


#=========================================
# DROP TABLES
#=========================================

print('1.  NFL_PROJECT Schema: Dropping Tables')
drop_cursor = mydb.cursor()

#order is important when dropping due to fk constraints
drop_cursor.execute('drop table if exists nfl_project.venues')
drop_cursor.execute('drop table if exists nfl_project.games')
drop_cursor.execute('drop table if exists nfl_project.pricing')



#=========================================
# CREATE TABLES
#=========================================

print('------------------------')
print('2.  NFL_PROJECT Schema: Creating tables')

mycursor = mydb.cursor()

#states table
mycursor.execute \
("create table nfl_project.venues \
  (venue_id int(10) not null\
  ,lat float \
  ,lon float \
  ,primary key (venue_id))")

mycursor.execute \
("create table nfl_project.games \
  (game_id int(10) not null\
  ,home varchar(20) \
  ,away varchar(20) \
  ,venue_id int(10)\
  ,date datetime\
  ,primary key (game_id))")

mycursor.execute \
("create table nfl_project.pricing \
  (game_id int(10) not null\
  ,low_price float \
  ,med_price float \
  ,high_price float \
  ,primary key (game_id))")

venueInsert = "INSERT INTO venues (venue_id, lat, lon) VALUES (%s, %s, %s)"
gameInsert = "INSERT INTO games (game_id, home, away, venue_id,date) VALUES ( %s, %s, %s, %s,%s)"
priceInsert = "INSERT INTO pricing (game_id, low_price, med_price, high_price) VALUES (%s, %s, %s, %s)"

venue = (1,23.4,54.1)
game =  (21,"packers","ravens",1,"1996-04-09")
price = (21,12,23,34)

mycursor.execute(venueInsert, venue)
mycursor.execute(gameInsert, game)
mycursor.execute(priceInsert, price)
mydb.commit()

print('------------------------')
print('--- Job Completed ---')

