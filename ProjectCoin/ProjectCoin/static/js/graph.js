// Used to store data to improve graph load times
var hourLoaded = false;
var dayLoaded = false;
var weekLoaded = false;
var monthLoaded = false;
var hourData = [];
var dayData = [];
var weekData = [];
var monthData = [];

function createHourGraph(coin) {
  if (!hourLoaded) {
    var endpoint = 'api/hourdata/'
    var defaultData = []
    var labels = [`low`, 'close', 'high'];
    $.ajax({
        method: "GET",
        url: endpoint,
        data: coin,
        success: function(result){
            defaultData = result
            hourData = result
            hourLoaded = true
            createGraph(defaultData)
        },
        error: function(err_data){
            console.log("error")
            console.log(err_data)
        }
    })
  } else {
    createGraph(hourData)
  }
}

function createDayGraph(coin) {
  if (!dayLoaded) {
    var endpoint = 'api/daydata/'
    var defaultData = []
    var labels = [`low`, 'close', 'high'];
    $.ajax({
        method: "GET",
        url: endpoint,
        data: coin,
        success: function(result){
            defaultData = result
            dayData = result
            dayLoaded = true
            createGraph(defaultData)
        },
        error: function(err_data){
            console.log("error")
            console.log(err_data)
        }
    })
  } else {
    createGraph(dayData)
  }
}

function createWeekGraph(coin) {
  if (!weekLoaded) {
    var endpoint = 'api/weekdata/'
    var defaultData = []
    var labels = [`low`, 'close', 'high'];
    $.ajax({
        method: "GET",
        url: endpoint,
        data: coin,
        success: function(result){
            defaultData = result
            weekData = result
            weekLoaded = true
            createGraph(defaultData)
        },
        error: function(err_data){
            console.log("error")
            console.log(err_data)
        }
    })
  } else {
    createGraph(weekData)
  }
}

function createMonthGraph(coin) {
  if (!monthLoaded) {
    var endpoint = 'api/monthdata/'
    var defaultData = []
    var labels = [`low`, 'close', 'high'];
    $.ajax({
        method: "GET",
        url: endpoint,
        data: coin,
        success: function(result){
            defaultData = result
            monthData = result
            monthLoaded = true
            createGraph(defaultData)
        },
        error: function(err_data){
            console.log("error")
            console.log(err_data)
        }
    })
  } else {
    createGraph(monthData)
  }
}

function createGraph(cryptoData){
    var close = [];
    var low = [];
    var high = [];
    var jsonData = JSON.parse(cryptoData);
    var tempData = jsonData.data;
    var indices = jsonData.index;
    var size = Object.keys(tempData).length;
    for (var a = 0; a < size; a++) {
        close.push(tempData[a][0]);
        low.push(tempData[a][2]);
        high.push(tempData[a][1]);
    }
    var g1 = document.getElementById("graph");
    var graph = new Chart(g1, {
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
    })
}
