function onClickedrank(){
    console.log("Jee rank predictor button clicked");
    var marks = document.getElementById("uimarks");
    var category = document.getElementById("uicategory");
    var rank = document.getElementById("uirank");
  
    var url = "http://127.0.0.1:5000/get_rank"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        marks: marks,
        category: category.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_category"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_category request");
        if(data) {
            var category = data.category;
            var uicategory = document.getElementById("uicategory");
            $('#uicategory').empty();
            for(var i in category) {
                var opt = new Option(category[i]);
                $('#category').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;
  