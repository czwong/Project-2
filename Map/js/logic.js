function createMap(marker) {
    // Define map layers
    var outdoormap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
        accessToken: API_KEY
    });

    var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v10/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
        accessToken: API_KEY
    });

    var satmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
        accessToken: API_KEY
    });

    // Define a baseMaps object to hold our base layers
    var baseMaps = {
        "Outdoor": outdoormap,
        "Dark": darkmap,
        "Satelitte": satmap
    };

    var football_events = L.layerGroup(marker);

    var overlayMaps = {
        "Football Events": football_events
    };

    var myMap = L.map("map", {
        center: [37.09, -95.71],
        zoom: 4,
        layers: [outdoormap, football_events]
    });

    // Create a layer control containing our baseMaps
    // Be sure to add an overlay Layer containing the football events
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);

    return myMap;
}

var today = new Date().getFullYear() + '-' + (new Date().getMonth() + 1) + '-' + new Date().getDate();
var page = 500;

url = `https://api.seatgeek.com/2/events?client_id=${client_id}&datetime_utc.gte=${today}&type=nfl&sort=datetime_utc.asc&per_page=${page}`;

d3.json(url, function (data) {
    var events = data.events;

    var eventMarker = [];

    var footballMarker = L.ExtraMarkers.icon({
        icon: 'fa-football-ball',
        markerColor: 'blue',
        shape: 'square',
        prefix: 'fas'
    });

    for (var i = 0; i < events.length; i++) {
        var event = events[i];

        var lat = event.venue.location.lat;
        var lng = event.venue.location.lon;

        eventMarker.push(L.marker([lat, lng], { icon: footballMarker })
            .bindPopup("<h2 align='center'>Game " + parseInt(i+1) + "<h2><hr><h3>" + event.short_title + "<h3>"));
    }

    var myMap = createMap(eventMarker);

    let counter = 0;
    var start_button = true;

    d3.select("#button-1").on("click", function () {
        if (counter > 0) {
            counter--
            myMap.flyTo(eventMarker[counter]._latlng, 10);
            eventMarker[counter].openPopup();
            console.log(redMarker);
        }
    });

    d3.select("#button-2").on("click", function () {
        if (start_button) {
            myMap.flyTo(eventMarker[counter]._latlng, 10);
            eventMarker[counter].openPopup();
            start_button = false;
        }

        else if (counter < eventMarker.length) {
            counter++;
            myMap.flyTo(eventMarker[counter]._latlng, 10);
            eventMarker[counter].openPopup();
        }
    });
});
