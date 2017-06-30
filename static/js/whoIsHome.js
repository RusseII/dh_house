namespace = '';
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

socket.on('house_occupants_updated', function(msg) {
  updateDOM(msg);
});

socket.on('connect_failed', function() {
    show_error("Error!", "Socket failed to connect.");
});

socket.on('reconnect_failed', function() {
    show_error("Error!", "Socket failed to reconnect.");
});

socket.on('connecting', function() {
    show_error("Connecting...", "Just a moment please.");
});

socket.on('reconnecting', function() {
    show_error("Reconnecting...", "Just a moment please.");
});

socket.on('error', function() {
    show_error("Error!", "Something isn't working right.");
});


function updateDOM(json) {
    hide_error();
    console.log(json);
    var Roos_is_home=(true);
    var Steve_is_home=(true);
    var Nick_is_home=(false);

    var Russell = document.getElementById("russell-home");
    var Steve = document.getElementById("steve-home");
    var Nick = document.getElementById("nick-home");

    if (Roos_is_home)
    {
        Russell.setAttribute('class',"home");
        Russell.inneHTML = 'Roos is home';
    } else {
        Russell.setAttribute('class',"away");
        Russell.inneHTML = 'Roos is not home';
    }

    if (Steve_is_home)
    {
        Steve.setAttribute('class',"home");
        Steve.inneHTML = 'Steve is home';
    } else {
        Steve.setAttribute('class',"away");
        Steve.inneHTML = 'Steve is not home';
    }

    if (Nick_is_home)
    {
        Nick.setAttribute('class',"home");
        Nick.inneHTML = 'Nick is home';
    } else {
        Nick.setAttribute('class',"away");
        Nick.inneHTML = 'Nick is not home';
    }

    // setTimeout(request_scan, 30000);
}

function request_scan() {
    //socket.emit('request_scan');
    var request = new XMLHttpRequest();
    request.open('GET', '/scan', true);

    request.onload = function() {
        if (this.status >= 200 && this.status < 400) {
            // Success!
            var data = JSON.parse(this.response);
            console.log(data);
            updateDOM(data);

        } else {
            // We reached our target server, but it returned an error
            show_error('Error', 'The server returned an error!');
        }
    };

    request.onerror = function() {
        // There was a connection error of some sort
        show_error('Error', 'Could not connect to the server');
    };

    request.send();
}

// Error things
var whoIsHomeErrorOverlay = document.querySelector("#who-is-home .overlay");
var whoIsHomeTitle = document.querySelector("#who-is-home .overlay-title");
var whoIsHomeMessage = document.querySelector("#who-is-home .overlay-message");

function hide_error() {
    whoIsHomeErrorOverlay.classList.add("hidden");
}

function show_error(title, message) {
    whoIsHomeErrorOverlay.classList.remove("hidden");
    whoIsHomeTitle.innerHTML = title;
    whoIsHomeMessage.innerHTML = message;
}