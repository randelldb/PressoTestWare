//////////////////////////////////////////////////////
var chart
var x = []
var data = []
var ctx = document.getElementById('a_chart').getContext('2d')
var chart_options = {
  type: 'line',
  data: {
    datasets: [
      {
        data: [],
        pointRadius: 0,
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        lineTension: 0,
        borderDash: [0, 0]
      }
    ]
  },
  options: {
    events: ['click'],
    tooltips: {
      enabled: false
    },
    scales: {
      xAxes: [
        {
          ticks: {
            display: false //this will remove only the label
          },
          type: 'realtime',
          realtime: {
            onRefresh: onRefresh,
            duration: 20000, // data in the past 20000 ms will be displayed
            refresh: 100, // onRefresh callback will be called every 1000 ms
            delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
            pause: false, // chart is not paused
            ttl: undefined // data will be automatically deleted as it disappears off the chart
          }
        }
      ],
      yAxes: [
        {
          ticks: {
            max: 6,
            min: 0,
            stepSize: 0.4
          }
        }
      ]
    },
    annotation: {
      annotations: [
        {
          type: 'line',
          id: 'bounds',
          mode: 'horizontal',
          scaleID: 'y-axis-0',
          value: 1,
          borderColor: 'rgb(255,140,0)',
          borderWidth: 2
        }
      ]
    }
  }
}

chart = new Chart(ctx, chart_options)

function onRefresh (chart) {
    chart.data.datasets.forEach(function (dataset) {
    $.getJSON('/modbusData', function (response) {
      dataset.data.push({
        x: Date.now(),
        y: response
      })
    })
  })
}

function set_bounds(id){
  console.log('Triggerd')
  $.getJSON('set_graph_bounds/' + id, function(get_bounds){
    chart.annotation.elements['bounds'].options.value = get_bounds['a_lvPlus']
    chart.update()
  })
}



////////////////////////////////////////////////////////////////
