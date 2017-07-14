
function get_weather() {
    show_error("Loading...", "Just a moment please.");
    //socket.emit('request_scan');
    var request = new XMLHttpRequest();
    console.log("test");
    request.open('GET', 'http://api.wunderground.com/api/0dae8a759154fd46/conditions/q/OH/Stow.json', false);

    console.log("test");

			request.send( null );
   			console.log(request.responseText)


            

       
    };


 
// Docs at http://simpleweatherjs.com

/* Does your browser support geolocation? */
if ("geolocation" in navigator) {
  $('.js-geolocation').show(); 
} else {
  $('.js-geolocation').hide();
}

/* Where in the world are you? */
$('.js-geolocation').on('click', function() {
  navigator.geolocation.getCurrentPosition(function(position) {
    loadWeather(position.coords.latitude+','+position.coords.longitude); //load weather using your lat/lng coordinates
  console.log("wtf")
  });
  console.log("wtf")
});

/* 
* Test Locations
* Austin lat/long: 30.2676,-97.74298
* Austin WOEID: 2357536
*/
$(document).ready(function() {
  loadWeather('Stow',''); //@params location, woeid
});

function loadWeather(location, woeid) {
  $.simpleWeather({
    location: location,
    woeid: woeid,
    unit: 'f',
    success: function(weather) {
      html = '<h2><i class="icon-'+weather.code+'"></i> '+weather.temp+'&deg;'+weather.units.temp+'</h2>';
      html += ''+weather.city+', '+weather.region+'';
      html += ''+weather.currently+'';
      
      html += '<div><button class="js-geolocation" style="display: none;">Use Your Locationas</button></div>';  
      
      
      $("#weather").html(html);
    },
    error: function(error) {
      $("#weather").html('<p>'+error+'</p>');
    }
  });
}
