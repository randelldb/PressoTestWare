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
  modbusCollector()
})

var modbusCollection = {}

var modbusCollector = function(){

  setInterval(() => {
    $.getJSON('/modbusData', function (response) {
      if (response == null){
      }else{
        modbusCollection = response
      }
    })
    // console.log(modbusCollection)
    // modbusTransporter()
    display_modbus_data()
  }, 200);
}


var modbusTransporter = function () {
  pressLoop = modbusCollection.press
  rvLoop = modbusCollection.rv
  tempLoop = modbusCollection.temp
  swtLoop = modbusCollection.switch

  $.ajax({
    url: '/modbusTransporter/' + pressLoop + '/' + rvLoop + '/' + tempLoop + '/' + swtLoop,
    type: 'get',
    success: function (response) {},
    error: function (xhr) {
      //Do Something to handle error
    }
  })
   
}

var display_modbus_data = function () {
  $('#rt_press').html(modbusCollection.press + ' Bar')
  $('#rt_rv').html(modbusCollection.rv + ' %')
  $('#rt_temp').html(modbusCollection.temp + ' °')
  $('#rt_switch').html(modbusCollection.switch)
}


var get_part_divider = function (NewID = 1) {
  $.ajax({
    url: '/get_part_divider/' + NewID,
    type: 'get',
    success: function (response) {
      $('#get_part_divider').html(response)
    },
    error: function (xhr) {}
  })
}


var controle_calibration = function () {
  $('.start_graph').click(function () {
    $(".start_graph").addClass("chartSelector-active").prop('disabled', true)
    var getId = $(this).attr('id')
    var stripId = getId.split('start_').pop()
    start_stop_chart(stripId, false)
   

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
    $(".start_graph").removeClass("chartSelector-active").prop('disabled', false)

    var getId = $(this).attr('id')
    var stripId = getId.split('stop_').pop()
    start_stop_chart(stripId, true)

    
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
      get_part_divider(NewID)
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
  // $.ajax({
  //   url: '/modbusData',
  //   type: 'get',
  //   success: function (response) {},
  //   error: function (xhr) {
  //     //Do Something to handle error
  //   }
  // })
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