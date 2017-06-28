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