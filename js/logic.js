console.log("is this a test")
window.onload=function(){
    var myMap = L.map("map", {
        center: [15.5994, -28.6731],
        zoom: 3
      });
      var el = document.getElementById('overlayBtn');
      if(el){
        el.addEventListener('click', swapper, false);
      }
      
      L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.streets-basic",
        accessToken: API_KEY
      }).addTo(myMap);
      
      mapboxgl.accessToken = API_KEY;
      var map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [-74.50, 40],
      zoom: 9
      });
      
      document.getElementById('fit').addEventListener('click', function() {
          map.fitBounds([[
          32.958984,
          -5.353521
          ], [
          43.50585,
          5.615985
          ]]);
          });
      }
var myMap = L.map("map", {
    center: [15.5994, -28.6731],
    zoom: 3
  });
  
  // Adding tile layer
  L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiamVzdXNnb20yOCIsImEiOiJjanZla2k0dDgwNnV1M3lwNDJpNGFxNXB0In0.PnpqwCU7ABXzWGM0AAgceQ").addTo(myMap);


// mapboxgl.accessToken = 'pk.eyJ1IjoiamVzdXNnb20yOCIsImEiOiJjanY5cjVhdDEwdnpxNDRuM2J1MG53ZmtsIn0.m3qmNNfUqJBmuceughFXiw';
// var map = new mapboxgl.Map({
// container: 'map', // container id
// style: 'mapbox://styles/mapbox/streets-v11', // stylesheet location
// center: [-74.50, 40], // starting position [lng, lat]
// zoom: 9 // starting zoom
// });

