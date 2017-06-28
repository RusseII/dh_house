function toggleTheme() {
	var el = document.body;
	var className = "light-theme";
	if (el.classList) {
		el.classList.toggle(className);
	} else {
		var classes = el.className.split(' ');
		var existingIndex = classes.indexOf(className);

		if (existingIndex >= 0)
			classes.splice(existingIndex, 1);
		else
			classes.push(className);

		el.className = classes.join(' ');
	}
}

function checkTime() {
	var d = new Date(); // for now
	var hour = d.getHours(); // => 9

	if (hour <= 20 || hour >= 7) {
		toggleTheme();
		console.log("Day Time!");
	}

	setTimeout(checkTime(), 600000);
}

var monthNames = [
	"Jan",
	"Feb",
	"Mar",
	"Apr",
	"May",
	"Jun",
	"Jul", 
	"Aug",
	"Sep",
	"Oct",
	"Nov",
	"Dec"
];

function getHoliday() {
	console.log("get holiday");
	var d = new Date();

	document.getElementById("holiday-month").innerHTML = monthNames[d.getMonth()];
	document.getElementById("holiday-date").innerHTML = d.getDate();

	sheetrock({
		url: "https://docs.google.com/spreadsheets/d/1tBK7fFFdpHt8BG3wL8uJ-qnjZShj3lIJ_amcAqQl8xI/edit#gid=0",
		query: "select A,C where A = '"+monthNames[d.getMonth()]+" "+d.getDate()+"'",
		callback: populateCal
	});
}

var populateCal = function (error, options, response) {
  var title = document.getElementById("holiday-title");
  console.log(response);
  if (!error) {
  	if (response.raw.table) {
  		if (response.raw.table.rows.length == 1) {
  			title.innerHTML = "Happy " + "<b>"+response.raw.table.rows[0].c[1].v + "</b>"+ "!";
  		} else {
  			var holidays = "";

  			for (var i = response.raw.table.rows.length - 1; i >= 1; i--) {
  				holidays += "<b>"+response.raw.table.rows[i].c[1].v + "</b>" + " & ";
  			}

  			holidays += "<b>"+response.raw.table.rows[0].c[1].v + "</b>";

  			title.innerHTML = "Happy " + holidays + "!";
  		}
  	}
   
  } else {
  	title.innerHTML = "Couldn't Load Holiday :(";
  	console.log(error);
  }

};

getHoliday();
