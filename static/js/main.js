function updateDOM(json) {
    var Roos_is_home=(json[0].room);
    var Steve_is_home=(json[1].room);
    var Nick_is_home=(json[2].room);

    var Russell = document.getElementById("russell-home");
    var Steve = document.getElementById("steve-home");
    var Nick = document.getElementById("nick-home");

    Russell.setAttribute('class',"home");
    Steve.setAttribute('class',"home");
    Nick.setAttribute('class',"home");

    if (Roos_is_home.indexOf('not')>0)
    {
        Russell.setAttribute('class',"away");
    }

    if (Steve_is_home.indexOf('not')>0)
    {
        Steve.setAttribute('class',"away");
    }

    if (Nick_is_home.indexOf('not')>0)
    {
        Nick.setAttribute('class',"away");
    }


    Russell.innerHTML = Roos_is_home;
    Steve.innerHTML=Steve_is_home;
    Nick.innerHTML=Nick_is_home;

    setTimeout(request_scan, 30000);
}

function request_scan() {
    var request = new XMLHttpRequest();
    request.open('GET', '/scan', true);

    request.onload = function() {
        if (this.status >= 200 && this.status < 400) {
            // Success!
            var data = JSON.parse(this.response);
            console.log(data);
            updateDOM(data);

            var el = document.querySelector("#who-is-home .error-overlay");
            el.classList.add("hidden");
        } else {
            // We reached our target server, but it returned an error

        }
    };

    request.onerror = function() {
        // There was a connection error of some sort
        var el = document.querySelector("#who-is-home .error-overlay");
        el.classList.remove("hidden");
    };

    request.send();
}