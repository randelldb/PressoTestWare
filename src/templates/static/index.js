$(document).ready(function () {
  console.log('ready!')

  get_model_data_list()
  get_printers()
  get_writers()
  get_ports()
  complete_calibration()
  get_count()
  start_calibration()

})

var start_calibration = function (){
  $('#start_a').click(function(){
    $.ajax({
      url: '/start_calibration',
      type: 'get',
      success: function (response) {
        
      },
      error: function (xhr) {
      }
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
    error: function (xhr) {
    }
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
