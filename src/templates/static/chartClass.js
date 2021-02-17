//////////////////////////////////////////////////////
data = [0]
var chart_options_a = {
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
    responsive: true,
    maintainAspectRatio: false,
    legend: {
      display: false
    },
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
            refresh: 1000, // onRefresh callback will be called every 1000 ms
            delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
            pause: false,
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
//////////////////////////////////////////////////////////
var chart_options_b = {
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
    responsive: true,
    maintainAspectRatio: false,
    legend: {
      display: false
    },
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
            pause: false,
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
          id: 'b_lvPlus',
          mode: 'horizontal',
          scaleID: 'y-axis-0',
          value: 1,
          borderColor: 'rgb(235, 131, 52)',
          borderWidth: 2
        },
        {
          type: 'line',
          id: 'b_lvMin',
          mode: 'horizontal',
          scaleID: 'y-axis-0',
          value: 1,
          borderColor: 'rgb(235, 131, 52)',
          borderWidth: 2
        },
        {
          type: 'line',
          id: 'b_hvPlus',
          mode: 'horizontal',
          scaleID: 'y-axis-0',
          value: 1,
          borderColor: 'rgb(235, 131, 52)',
          borderWidth: 2
        },
        {
          type: 'line',
          id: 'b_hvMin',
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
////////////////////////////////////////////////
var cta = document.getElementById('a_chart').getContext('2d')
chart_a = new Chart(cta, chart_options_a)

function onRefresh (chart) {
  chart.data.datasets.forEach(function (dataset) {
    $.getJSON('/modbusData', function (response) {
      dataset.data.push({
        x: Date.now(),
        y: response.press
      })
    })
  })
}

function set_bounds (id = 1) {
  get_model_data(id)
  $.getJSON('set_graph_bounds/' + id, function (get_bounds) {
    chart_a.annotation.elements['a_lvPlus'].options.value =
      get_bounds['a_lvPlus']
    chart_a.annotation.elements['a_lvMin'].options.value = get_bounds['a_lvMin']
    chart_a.annotation.elements['a_hvPlus'].options.value =
      get_bounds['a_hvPlus']
    chart_a.annotation.elements['a_hvMin'].options.value = get_bounds['a_hvMin']

    chart_a.options.scales = {
      xAxes: [
        {
          ticks: {
            display: false //this will remove only the label
          },
          type: 'realtime',
          realtime: {
            duration: 20000, // data in the past 20000 ms will be displayed
            refresh: 100, // onRefresh callback will be called every 1000 ms
            delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
            pause: false,
            ttl: undefined // data will be automatically deleted as it disappears off the chart
          }
        }
      ],
      yAxes: [
        {
          ticks: {
            max: get_bounds['a_hvPlus'] + 1,
            min: get_bounds['a_lvMin'] - 1,
            stepSize: 1
          }
        }
      ]
    }
  })
}

function set_bounds_b (id = 1) {
  get_model_data(id)
  $.getJSON('set_graph_bounds/' + id, function (get_bounds) {
    chart_b.annotation.elements['b_lvPlus'].options.value =
      get_bounds['b_lvPlus']
    chart_b.annotation.elements['b_lvMin'].options.value = get_bounds['b_lvMin']
    chart_b.annotation.elements['b_hvPlus'].options.value =
      get_bounds['b_hvPlus']
    chart_b.annotation.elements['b_hvMin'].options.value = get_bounds['b_hvMin']

    chart_b.options.scales = {
      xAxes: [
        {
          ticks: {
            display: false //this will remove only the label
          },
          type: 'realtime',
          realtime: {
            duration: 20000, // data in the past 20000 ms will be displayed
            refresh: 1000, // onRefresh callback will be called every 1000 ms
            delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
            pause: false,
            ttl: undefined // data will be automatically deleted as it disappears off the chart
          }
        }
      ],
      yAxes: [
        {
          ticks: {
            max: get_bounds['b_hvPlus'] + 1,
            min: get_bounds['b_lvMin'] - 1,
            stepSize: 1
          }
        }
      ]
    }
  })
}

var deel_a = function(){
  
}

var deel_b = function(){
  chart_a.destroy();
  set_bounds_b()
  $("#a_chart").css('display','none')
  $(".deel_a").css('display','none')
  $(".deel_b").css('display','block')
  var ctb = document.getElementById('b_chart').getContext('2d')
  chart_b = new Chart(ctb, chart_options_b)
}


////////////////////////////////////////////////////////////////
