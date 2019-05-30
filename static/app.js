function footballdata(team) {
    // @TODO: Complete the following function that builds the metadata panel
    // Use `d3.json` to fetch the metadata for a sample
    var url = "/games/" + `${team}`;

    // Use d3 to select the panel with id of `#sample-metadata`
    var football_data = d3.select("#footballdata");

    d3.json(url).then(function (response) {
        // Use `.html("") to clear any existing metadata
        football_data.html("");

        var cell = football_data.append("p");
        cell.html('<b>Number of Games: </b>' + response.length);
    });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#dataSet");

  // Use the list of sample names to populate the select options
  d3.json("/teams").then((team_list) => {
    team_list.forEach((team) => {
      selector
        .append("option")
        .text(team)
        .property("value", team);
    });

      // Use the first sample from the list to build the initial plots
      const firstteam = team_list[0][0];
      footballdata(firstteam);
  });
}

// Initialize the dashboard
init();

function optionChanged(newTeam) {
    // Fetch new data each time a new sample is selected
    footballdata(newTeam);
}

$('select').on('change', function () {
    var team = this.value;
    localStorage.setItem("x", team);
});