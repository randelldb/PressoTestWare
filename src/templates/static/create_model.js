$(document).ready(function () {
  get_model_data_list()
})

// get data for dropdown
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
    url: '/get_model_form_data/' + id,
    type: 'get',
    success: function (response) {
      $('#get_model_form_data').html(response)
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}

var model_update = function (id) {
  console.log('in js fn')
  console.log(id)
  var modelName = $('#modelName').val()
  var brand = $('#brand').val()
  var model = $('#model').val()
  var customer = $('#customer').val()
  var ref = $('#ref').val()

  var type_a = 1

  var a_highValue = $('#a_highValue').val()
  var b_highValue = $('#b_highValue').val()
  var a_hvPlus = $('#a_hvPlus').val()
  var a_hvMin = $('#a_hvMin').val()
  var b_hvPlus = $('#b_hvPlus').val()
  var b_hvMin = $('#b_hvMin').val()

  var type_b = 2

  var a_lowValue = $('#a_lowValue').val()
  var b_lowValue = $('#b_lowValue').val()
  var a_lvPlus = $('#a_lvPlus').val()
  var a_lvMin = $('#a_lvMin').val()
  var b_lvPlus = $('#b_lvPlus').val()
  var b_lvMin = $('#b_lvMin').val()

  $.ajax({
    url: '/model_update/' + id,
    type: 'post',
    data: {
      id: id,
      modelName: modelName,
      brand: brand,
      model: model,
      customer: customer,
      ref: ref,

      type_a: type_a,

      a_highValue: a_highValue,
      b_highValue: b_highValue,
      a_hvPlus: a_hvPlus,
      a_hvMin: a_hvMin,
      b_hvPlus: b_hvPlus,
      b_hvMin: b_hvMin,

      type_b: type_b,

      a_lowValue: a_lowValue,
      b_lowValue: b_lowValue,
      a_lvPlus: a_lvPlus,
      a_lvMin: a_lvMin,
      b_lvPlus: b_lvPlus,
      b_lvMin: b_lvMin
    },
    success: function (response) {
      console.log('Js updated')
      location.reload()
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}
