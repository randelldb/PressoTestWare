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
            max: 10,
            min: 0,
            stepSize: 1
          }
        }
      ]
    },
    annotation: {
      annotations: [
        {
          type: 'line',
          id: 'a_lvPlus',
          mode: 'horizontal',
          scaleID: 'y-axis-0',
          value: 1,
          borderColor: 'rgb(235, 131, 52)',
          borderWidth: 2
        },
        {
          type: 'line',
          id: 'a_lvMin',
          mode: 'horizontal',
          scaleID: 'y-axis-0',
          value: 1,
          borderColor: 'rgb(235, 131, 52)',
          borderWidth: 2
        },
        {
          type: 'line',
          id: 'a_hvPlus',
          mode: 'horizontal',
          scaleID: 'y-axis-0',
          value: 1,
          borderColor: 'rgb(235, 131, 52)',
          borderWidth: 2
        },
        {
          type: 'line',
          id: 'a_hvMin',
          mode: 'horizontal',
          scaleID: 'y-axis-0',
          value: 1,
          borderColor: 'rgb(235, 131, 52)',
          borderWidth: 2
        }
      ]
    }
  }
}

chart = new Chart(ctx, chart_options)

function onRefresh (chart) {
    chart.data.datasets.forEach(function (dataset) {
    $.getJSON('/modbusDebug', function (response) {
      dataset.data.push({
        x: Date.now(),
        y: response.rv
      })
    })
  })
}

function set_bounds(id){
  console.log('Triggerd')
  get_model_data(id)
  $.getJSON('set_graph_bounds/' + id, function(get_bounds){
    chart.annotation.elements['a_lvPlus'].options.value = get_bounds['a_lvPlus']
    chart.annotation.elements['a_lvMin'].options.value = get_bounds['a_lvMin']
    chart.annotation.elements['a_hvPlus'].options.value = get_bounds['a_hvPlus']
    chart.annotation.elements['a_hvMin'].options.value = get_bounds['a_hvMin']

    chart.options.scales = {
      yAxes: [{
          display: true,
          ticks: {
            max: get_bounds['a_hvPlus'] + 1,
            min: get_bounds['a_lvMin'] - 1,
            stepSize: 1
          }
      }]
  };

    chart.update()
  })
}



////////////////////////////////////////////////////////////////
