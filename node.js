var mysql = require('mysql');

var conn = createConnection({
    user: 'root',
    password: 'root',
    server: 'project2', 
    database: 'nflPproject' 
});

con.connect(function(err) {
    if (err) throw err;
    con.query("SELECT team1, team2, low_price, med_price, high_price from games join pricing on games.game_id=pricing.game_id where team1='{team_choice}' or team2='{team_choice}' order by utcdate;", function (err, result, fields) {
      if (err) throw err;
      console.log(result);
    });
  });


