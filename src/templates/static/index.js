$(document).ready(function () {
  console.log('ready!')

  get_model_data_list()
  get_model_data()
  get_printers()
  get_writers()
  get_ports()
  complete_calibration()
  get_count()
  controle_calibration()
  display_modbus_data()
})

var display_modbus_data = function () {
  setInterval(function(){
  $.getJSON('/modbusData', function (response) {
    $('#rt_press').html(response.press + ' Bar')
    $('#rt_rv').html(response.rv + ' %')
    $('#rt_temp').html(response.temp + ' °')
    $('#rt_switch').html(response.switch)
  })
  }, 100)
}

var controle_calibration = function () {
  $('.start_graph').click(function () {
    var getId = $(this).attr('id')
    var stripId = getId.split('start_').pop()
    $.ajax({
      url: '/run/' + stripId,
      type: 'get',
      success: function (response) {
        console.log('start:' + stripId)
      },
      error: function (xhr) {}
    })
  })

  $('.stop_graph').click(function () {
    var getId = $(this).attr('id')
    var stripId = getId.split('stop_').pop()
    $.ajax({
      url: '/stop/' + stripId,
      type: 'get',
      success: function (response) {
        console.log('stop:' + stripId)
      },
      error: function (xhr) {}
    })
  })
}

var get_model_data = function (NewID = 1) {
  $.ajax({
    url: '/get_model_data/' + NewID,
    type: 'get',
    success: function (response) {
      $('.get_model_data').html(response)
    },
    error: function (xhr) {}
  })
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

var set_printer = function (selectedPrinter) {
  $.ajax({
    url: '/set_printer/' + selectedPrinter,
    type: 'get',
    success: function (response) {},
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

var set_writer = function (selectedWriter) {
  $.ajax({
    url: '/set_writer/' + selectedWriter,
    type: 'get',
    success: function (response) {},
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}
