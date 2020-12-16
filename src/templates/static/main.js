$(document).ready(function () {
  console.log('ready!')

  // var interval = 500 // where X is your every X minutes
  // setInterval(modbusCall, interval)
  get_model_data()
  get_model_preset()
  get_ports()
  modbusCall()
  chart_aside()
  chart_bside()
})

/////////////////////////////////////////////////////// convert later to class//////////////////////////////////

var chart_aside = function () {
  var data = []
  var options = {
    chart: {
      type: 'line',
      toolbar: false
    },
    series: [
      {
        name: 'bar',
        data: data
      }
    ]
  }

  var chart = new ApexCharts(document.querySelector('#a_chart'), options)
  chart.render()

  window.setInterval(function () {
    $.getJSON('http://127.0.0.1:5000/modbusData'),
      function (response) {
        data.push(response)
        console.log(response)
        console.log('response')

        chart.updateSeries([
          {
            name: 'bar',
            data: data
          }
        ])
      }
  }, 1000)
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

var chart_bside = function () {
  var options = {
    chart: {
      type: 'line',
      toolbar: false
    },
    series: [
      {
        name: 'sales',
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125]
      }
    ],
    xaxis: {
      categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
    }
  }

  var chart = new ApexCharts(document.querySelector('#b_chart'), options)

  chart.render()
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

var get_model_data = function () {
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

var get_model_preset = function (id = 1) {
  $.ajax({
    url: '/get_model_preset/' + id,
    type: 'get',
    success: function (response) {
      $('.model_preset').html(response)
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
