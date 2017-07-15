
function acceptFlightNo() {
    var latitude, longitude;
    var flightNo = document.getElementById("flightNoTextbox").value;
    var flightNoPacked = escape(flightNo);
    var e = document.getElementById("selectClass");
    var flightClass = e.options[e.selectedIndex].value;
    var flightClassPacked = escape(flightClass);
    window.document.location = 'Page2.html?' + flightNoPacked + "," + flightClassPacked;
}

