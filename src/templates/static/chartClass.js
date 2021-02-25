rate = 200
durationttl = 20000
b_active = 0
active_id = 1

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
    animation: {
      duration: 0
    },
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
            duration: durationttl, // data in the past 20000 ms will be displayed
            refresh: rate, // onRefresh callback will be called every 1000 ms
            delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
            pause: true,
            ttl: durationttl // data will be automatically deleted as it disappears off the chart
          }
        }
      ],
      yAxes: [
        {
          ticks: {
            // suggestedMax: 10,
            // suggestedMin: 0,
            min: 0,
            max: 10,
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
    animation: {
      duration: 0
    },
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
            duration: durationttl, // data in the past 20000 ms will be displayed
            refresh: rate, // onRefresh callback will be called every 1000 ms
            delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
            pause: true,
            ttl: durationttl // data will be automatically deleted as it disappears off the chart
          }
        }
      ],
      yAxes: [
        {
          ticks: {
            // suggestedMax: 10,
            // suggestedMin: 0,
            min: 0,
            max: 10,
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
    // $.getJSON('/modbusData', function (response) {
    //   dataset.data.push({
    //     x: Date.now(),
    //     y: response.press
    //   })
    // })
    // dataset.data.push({
    //     x: Date.now(),
    //     y: modbusCollection.press
    //   })
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
            onRefresh: onRefresh,
            duration: durationttl, // data in the past 20000 ms will be displayed
            refresh: rate, // onRefresh callback will be called every 1000 ms
            delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
            pause: false,
            ttl: durationttl // data will be automatically deleted as it disappears off the chart
          }
        }
      ],
      yAxes: [
        {
          ticks: {
            // suggestedMax: get_bounds['a_hvPlus'] + 1,
            // suggestedMin: get_bounds['a_lvMin'] - 1,
            max: get_bounds['a_hvPlus'] + 1,
            min: get_bounds['a_lvMin'] - 1,
            stepSize: 0.2
          }
        }
      ]
    }
  })
}

function set_bounds_b (id = 1) {
  //get_model_data(id)
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
            onRefresh: onRefresh,
            duration: durationttl, // data in the past 20000 ms will be displayed
            refresh: rate, // onRefresh callback will be called every 1000 ms
            delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
            pause: false,
            ttl: durationttl // data will be automatically deleted as it disappears off the chart
          }
        }
      ],
      yAxes: [
        {
          ticks: {
            // suggestedMax: get_bounds['b_hvPlus'] + 1,
            // suggestedMin: get_bounds['b_lvMin'] - 1,
            max: get_bounds['b_hvPlus'] + 1,
            min: get_bounds['b_lvMin'] - 1,
            stepSize: 0.2
          }
        }
      ]
    }
  })
}

var reset = function (id = active_id) {
  $('#deel_a').addClass('chartSelector-active')
  $('#deel_b').removeClass('chartSelector-active')
  $('#deel_a').prop('disabled', false)
  get_model_data(id)
  active_id = id
  //set_bounds(id)

  $('#a_chart').css('display', 'block')
  $('.deel_a').css('display', 'block')
  $('.deel_b').css('display', 'none')
  chart_a.destroy()
  if ( b_active == 1) {

    chart_b.destroy()
 }
  

  var cta = document.getElementById('a_chart').getContext('2d')
  chart_a = new Chart(cta, chart_options_a)
}

var deel_b = function () {
  $('#deel_a').removeClass('chartSelector-active')
  $('#deel_a').prop('disabled', true)
  $('#deel_b').addClass('chartSelector-active')

  chart_a.destroy()

  $('#a_chart').css('display', 'none')
  $('.deel_a').css('display', 'none')
  $('.deel_b').css('display', 'block')

  var ctb = document.getElementById('b_chart').getContext('2d')
  chart_b = new Chart(ctb, chart_options_b)
  b_active = 1
}

var start_stop_chart = function(selector, action){
  if(selector == 'a' && action == false){
    set_bounds(active_id)
  }else if(selector == 'b' && action == false){
    set_bounds_b(active_id)
  }else if(action == true){
    chart_a.options.scales = {
      xAxes: [
        {
          ticks: {
            display: false //this will remove only the label
          },
          type: 'realtime',
          realtime: {
            onRefresh: onRefresh,
            duration: durationttl, // data in the past 20000 ms will be displayed
            refresh: rate, // onRefresh callback will be called every 1000 ms
            delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
            pause: true,
            ttl: durationttl // data will be automatically deleted as it disappears off the chart
          }
        }
      ]
    }

    if(b_active == 1){
      chart_b.options.scales = {
        xAxes: [
          {
            ticks: {
              display: false //this will remove only the label
            },
            type: 'realtime',
            realtime: {
              onRefresh: onRefresh,
              duration: durationttl, // data in the past 20000 ms will be displayed
              refresh: rate, // onRefresh callback will be called every 1000 ms
              delay: 0, // delay of 1000 ms, so upcoming values are known before plotting a line
              pause: true,
              ttl: durationttl // data will be automatically deleted as it disappears off the chart
            }
          }
        ]
      }
    }
  }
}

// set_bounds()
////////////////////////////////////////////////////////////////
