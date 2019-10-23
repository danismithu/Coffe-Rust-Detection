function predict() {
  var form_data = new FormData($('#upload-file')[0]);

  el("analyze-button").innerHTML = "Analyzing...";

  $.ajax({
    type: 'POST',
    url: '/predict',
    data: form_data,
    contentType: false,
    processData: false,
    async: true,
    success: function(data) {
      window.alert('Prediction is: ' + data);
    },
  });
}
