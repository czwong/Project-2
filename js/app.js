var tableData = data;

var submit = d3.select("#filter-btn");
var clear = d3.select("#clear-btn");


var dropDownField = d3.select("#dataSet");

dropDownField.on("click", function () {
    currentSel = d3.event.target.value;
    
    console.log("change-current dropdown selection is : " + currentSel);
});

