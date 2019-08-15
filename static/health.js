

function handleChange() {
  d3.json("static/data/health_problem.json").then (data => {
    console.log(data);
    
  // grab the value of the input field
  
  var inputText = document.getElementById("problem");
  console.log(inputText.value);
  
var filterData= data.filter(row => row.ID==inputText.value);

var consumeOutput = d3.select("#consume");
var avoidOutput = d3.select("#avoid");

consumeOutput.text(filterData[0]['Consume']);
avoidOutput.text(filterData[0]["Avoid"]);
});
};



