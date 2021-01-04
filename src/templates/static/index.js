var gid

$(document).ready(function () {
  console.log('ready!')
  var CurrentId = 1

  get_model_data_list()
  get_printers()
  get_writers()
  get_ports()
  complete_calibration()
  get_count()
  a_chart()
})

var get_model_data = function (NewID = 1) {
  CurrentId = NewID
  $.ajax({
    url: '/get_model_data/' + NewID,
    type: 'get',
    success: function (response) {
      $('.get_model_data').html(response)
      gid = NewID

    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}

var a_chart = function () {

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
            mode: 'horizontal',
            scaleID: 'y-axis-0',
            value: x = [],
            borderColor: 'rgb(255,140,0)',
            borderWidth: 2
          }
        ]
      }
    }
  }

  chart = new Chart(ctx, chart_options)

  function onRefresh (chart) {

    $.getJSON('/set_graph_bounds/' + gid, function (response) {
      z = response['a_hvPlus']
    })

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

var validate_hv = function () {
  $.ajax({
    url: '/validate_hv',
    type: 'get',
    success: function (response) {
      $('.get_model_data').html(response)
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
        get_count()
      },
      error: function (xhr) {
        //Do Something to handle error
      }
    })
  })
}

var modbusCall = function () {
  $.ajax({
    url: '/modbusData',
    type: 'get',
    success: function (response) {},
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
    success: function (response) {},
    error: function (xhr) {
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

var get_writers = function () {
  $.ajax({
    url: '/get_writers',
    type: 'get',
    success: function (response) {
      $("[aria-labelledby='label_writer']").html(response)
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}
