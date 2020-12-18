$(document).ready(function () {
  console.log('ready!')

  get_model_data_list()
  get_model_data()
  get_printers()
  get_ports()
  set_certificate()
  complete_calibration()
  get_count()
})

var get_count = function () {
  $.ajax({
    url: '/get_count',
    type: 'get',
    success: function (response) {
      $('#get_counter').html(response)
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}

var complete_calibration = function () {
  $('#complete_calibration').click(function (event) {
    $.ajax({
      url: '/complete_calibration',
      type: 'get',
      success: function (response) {
        console.log(response)
        get_count()
      },
      error: function (xhr) {
        //Do Something to handle error
      }
    })
  })
}

var set_certificate = function () {
  $('#set_certificate').submit(function (event) {
    event.preventDefault()
    var r_a_hi = $('#r_a_hi').val()
    var r_a_lo = $('#r_a_lo').val()
    var temp_a = $('#temp_a').val()
    var rv_a = $('#rv_a').val()
    var r_b_hi = $('#r_b_hi').val()
    var r_b_lo = $('#r_b_lo').val()
    var temp_b = $('#temp_b').val()
    var rv_b = $('#rv_b').val()

    $.ajax({
      url: '/set_certificate',
      type: 'post',
      data: {
        r_a_hi: r_a_hi,
        r_a_lo: r_a_lo,
        temp_a: temp_a,
        rv_a: rv_a,
        r_b_hi: r_b_hi,
        r_b_lo: r_b_lo,
        temp_b: temp_b,
        rv_b: rv_b
      },
      success: function (response) {
        console.log('pass')
      },
      error: function (xhr) {
        //Do Something to handle error
      }
    })
  })
}

var a_chart = function (id) {
  var hvPlus = []
  $.getJSON('/set_graph_bounds/1', function (response) {
    console.log(response)
    hvPlus = [response]
    console.log(hvPlus)
  })

  var ctx = document.getElementById('a_chart').getContext('2d')
  var chart = new Chart(ctx, {
    type: 'line',
    data: {
      datasets: [
        {
          data: [],
          pointRadius: 0,
          label: 'Dataset 1',
          borderColor: 'rgb(255, 99, 132)',
          backgroundColor: 'rgba(255, 99, 132, 0.5)',
          lineTension: 0,
          borderDash: [0, 0]
        },
        {
          data: [2.0],
          pointRadius: 0,
          label: 'Dataset 2',
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
              max: 5,
              min: 0,
              stepSize: 0.5
            }
          }
        ]
      }
    }
  })
  var data = []
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
}

var b_chart = function () {
  var ctx = document.getElementById('b_chart').getContext('2d')
  var chart = new Chart(ctx, {
    type: 'line',
    data: {
      datasets: [
        {
          data: [],
          pointRadius: 0,
          label: 'Dataset 1',
          borderColor: 'rgb(255, 99, 132)',
          backgroundColor: 'rgba(255, 99, 132, 0.5)',
          lineTension: 0,
          borderDash: [0, 0]
        },
        {
          data: [2.0],
          pointRadius: 0,
          label: 'Dataset 2',
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
              max: 5,
              min: 0,
              stepSize: 0.5
            }
          }
        ]
      }
    }
  })
  var data = []
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
}

var modbusCall = function () {
  $.ajax({
    url: '/modbusData',
    type: 'get',
    success: function (response) {
      console.log('from ajax call')
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}

var get_model_data_list = function () {
  $.ajax({
    url: '/get_calibration_model',
    type: 'get',
    success: function (response) {
      $("[aria-labelledby='select_model']").html(response)
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}

var get_model_data = function (id = 1) {
  $.ajax({
    url: '/get_model_data/' + id,
    type: 'get',
    success: function (response) {
      $('.get_model_data').html(response)
      a_chart(id)
      b_chart(id)
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}

var get_ports = function () {
  $.ajax({
    url: '/get_ports',
    type: 'get',
    success: function (response) {
      $("[aria-labelledby='select_com']").html(response)
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}

var set_ports = function (id) {
  $.ajax({
    url: '/set_ports/' + id,
    type: 'get',
    success: function (response) {
      console.log('pass')
      //$(".model_preset").html(response);
    },
    error: function (xhr) {
      console.log('js error')
      //Do Something to handle error
    }
  })
}

var get_printers = function () {
  $.ajax({
    url: '/get_printers',
    type: 'get',
    success: function (response) {
      $("[aria-labelledby='main_printer']").html(response)
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}
