$(document).ready(function () {
  get_model_data()
})


// get data for dropdown
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

var get_model_form_data = function (id = 1) {
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

var model_delete = function (id) {
  $.ajax({
    url: '/model_delete',
    type: 'get',
    success: function (response) {
      $("[aria-labelledby='select_model']").html(response)
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}
