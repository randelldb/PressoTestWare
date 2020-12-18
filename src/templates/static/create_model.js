$(document).ready(function () {
  get_model_data()
})

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
    url: '/get_model_update/' + id,
    type: 'get',
    success: function (response) {
      $('#get_model_update').html(response)
    },
    error: function (xhr) {
      //Do Something to handle error
    }
  })
}
