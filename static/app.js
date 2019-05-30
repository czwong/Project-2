function footballdata(team) {
    var url = "/games/" + `${team}`;

    // Use d3 to select the panel with id of `#gamedata`
    var football_data = d3.select("#gamedata");

    d3.json(url).then(function (response) {
        // Use `.html("") to clear any existing metadata
        football_data.html("");

        football_data.html('<b>Number of Games: </b>' + response.length);
        //cell.html('<b>Number of Games: </b>' + response.length);
    });
}

function boxplot(team) {
    var url = "/prices/" + `${team}`;

    var boxplot = d3.select("#boxplot");

    d3.json(url).then(function (data) {
        boxplot.html("");

        var low = [];
        var med = [];
        var high = [];

        for (var i = 0; i < data.length; i++) {
            low.push(data[i].Low_price);
            med.push(data[i].Med_price);
            high.push(data[i].High_price);
        }

        var trace1 = {
            x: low,
            type: 'box',
            marker: { color: 'green' },
            name: 'Low Price'
        };

        var trace2 = {
            x: med,
            type: 'box',
            marker: { color: 'yellow' },
            name: 'Med Price'
        };

        var trace3 = {
            x: high,
            type: 'box',
            marker: { color: 'red' },
            name: 'High Price'
        };

        var data1 = [trace1];
        var data2 = [trace2];
        var data3 = [trace3];

        var layout = {
            margin: {
                t: 10,
                l: 80,
                r: 30,
                b: 20
            },
            autosize: false,
            width: 700,
            height: 100,
            paper_bgcolor: '#F5F5F5',
            plot_bgcolor: '#D3D3D3'
        };

        Plotly.newPlot('boxplot1', data1, layout)
        Plotly.newPlot('boxplot2', data2, layout)
        Plotly.newPlot('boxplot3', data3, layout)
    });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#dataSet");

  // Use the list of teams to populate the select options
  d3.json("/teams").then((team_list) => {
    team_list.forEach((team) => {
      selector
        .append("option")
        .text(team)
        .property("value", team);
    });

      // Use the first team from the list to build the initial plots
      const firstteam = team_list[0][0];
      footballdata(firstteam);
      boxplot(firstteam);
  });
}

// Initialize the dashboard
init();

function optionChanged(newTeam) {
    // Fetch new data each time a new team is selected
    footballdata(newTeam);
    boxplot(newTeam);
}

//d3.select('#refresh-btn').on("click", function () {
        
//})

$('select').on('change', function () {
    var team = this.value;
    localStorage.setItem("x", team);
});