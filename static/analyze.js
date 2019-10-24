var el = x => document.getElementById(x);

function showPicker() {
  el("file-input").click();
}

function showPicked(input) {
  el("upload-label").innerHTML = input.files[0].name;
  var reader = new FileReader();
  reader.onload = function(e) {
    el("image-picked").src = e.target.result;
    el("image-picked").className = "";
  };
  reader.readAsDataURL(input.files[0]);
}

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
      el("result-label").innerHTML = 'Prediction is: ' + data;
      $("#upload-button").hide();
      $("#analyze-button").hide();
    },
  });
}
