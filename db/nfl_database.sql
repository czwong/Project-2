/* Team List */
SELECT team1 FROM nfl_project.games
GROUP BY team1;

/* Individual Schedule Ordered by Date */
select title, lat, lon from games
join venues on games.venue_id=venues.venue_id
where team1="Chicago Bears" or team2="Chicago Bears"
order by utcdate;

/* Season Pricing Ordered by Date*/
select title, team1, team2, med_price from games
join pricing on games.game_id=pricing.game_id
where team1="Chicago Bears" or team2="Chicago Bears"
order by utcdate

