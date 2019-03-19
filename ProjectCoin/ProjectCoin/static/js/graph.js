// Used to store data to improve graph load times
var hourLoaded = false;
var dayLoaded = false;
var weekLoaded = false;
var monthLoaded = false;
var hourData = [];
var dayData = [];
var weekData = [];
var monthData = [];
var hourIndices = [];
var dayIndices = [];
var weekIndices = [];
var monthIndices = [];
var g1 = document.getElementById("graph");
var loaded = false;
var graph = [];

function createHourGraph(coin) {
  if (!hourLoaded) {
    var endpoint = 'api/hourdata/';
    var labels = ['low', 'close', 'high'];
    var dt = 'minute';
    $.ajax({
        method: "GET",
        url: endpoint,
        data: coin,
        success: function(result){
            hourData = result;
            var jsonData = JSON.parse(result);
            var indices = jsonData.index;
            var size = Object.keys(indices).length;
            for (var a = 0; a < size; a++) {
                var time = indices[a].substring(14, 19);
                var hour = indices[a].substring(11, 13);
                hour = Number(hour);
                if (hour < 12) {
                    time += " AM";
                } else {
                    time += " PM";
                }
                hourIndices.push(time);
            }
            createGraph(hourData, hourIndices);
            hourLoaded = true;
        },
        error: function(err_data){
            console.log("error")
            console.log(err_data)
        }
    })
  } else {
    createGraph(hourData, hourIndices);
  }
}

function createDayGraph(coin) {
  if (!dayLoaded) {
    var endpoint = 'api/daydata/'
    var labels = ['low', 'close', 'high'];
    $.ajax({
        method: "GET",
        url: endpoint,
        data: coin,
        success: function(result){
            dayData = result;
            var jsonData = JSON.parse(result);
            var indices = jsonData.index;
            var size = Object.keys(indices).length;
            for (var a = 0; a < size; a++) {
                var time = indices[a].substring(11, 19);
                var hour = indices[a].substring(11, 13);
                hour = Number(hour);
                if (hour < 12) {
                    dayIndices.push(time + " AM");
                } else {
                    dayIndices.push(time + " PM");
                }
            }
            createGraph(dayData, dayIndices);
            dayLoaded = true;
        },
        error: function(err_data){
            console.log("error")
            console.log(err_data)
        }
    })
  } else {
    createGraph(dayData, dayIndices);
  }
}

function createWeekGraph(coin) {
  if (!weekLoaded) {
    var endpoint = 'api/weekdata/'
    var labels = ['low', 'close', 'high'];
    $.ajax({
        method: "GET",
        url: endpoint,
        data: coin,
        success: function(result){
            weekData = result;
            var jsonData = JSON.parse(result);
            var indices = jsonData.index
            var size = Object.keys(indices).length;
            for (var a = 0; a < size; a++) {
                weekIndices.push(indices[a].substring(0, 10));
            }
            createGraph(weekData, weekIndices);
            weekLoaded = true;
        },
        error: function(err_data){
            console.log("error")
            console.log(err_data)
        }
    })
  } else {
    createGraph(weekData, weekIndices);
  }
}

function createMonthGraph(coin) {
  if (!monthLoaded) {
    var endpoint = 'api/monthdata/'
    var labels = ['low', 'close', 'high'];
    $.ajax({
        method: "GET",
        url: endpoint,
        data: coin,
        success: function(result){
            monthData = result;
            var jsonData = JSON.parse(result);
            var indices = jsonData.index
            var size = Object.keys(indices).length;
            for (var a = 0; a < size; a++) {
                monthIndices.push(indices[a].substring(0, 10));
            }
            createGraph(monthData, monthIndices);
            monthLoaded = true;
        },
        error: function(err_data){
            console.log("error")
            console.log(err_data)
        }
    })
  } else {
    createGraph(monthData, monthIndices);
  }
}

function createGraph(cryptoData, indices) {
    var close = [];
    var low = [];
    var high = [];
    var jsonData = JSON.parse(cryptoData);
    var tempData = jsonData.data;
    var size = Object.keys(tempData).length;
    for (var a = 0; a < size; a++) {
        close.push(tempData[a][0]);
        low.push(tempData[a][2]);
        high.push(tempData[a][1]);
    }
    var trend = close[size - 1] - close[0];
    var trendPercent = trend / close[0];
    if (loaded) {
      graph.destroy();
    }
    graph = new Chart(g1, {
        type: 'line',
        data: {
            labels: indices,
            datasets: [
              {
                label: "Close",
                data: close,
                fill: false,
                borderColor: 'rgba(0, 0, 0, 1)',
                lineTension: 0
              },
              {
                label: "Low",
                data: low,
                fill: false,
                borderColor: 'rgba(255, 165, 0, 1)',
                lineTension: 0
              },
              {
                label: "High",
                data: high,
                fill: false,
                borderColor: 'rgba(0, 255, 0, 1)',
                lineTension: 0
              }
            ]
        }
    });
    loaded = true;
}
