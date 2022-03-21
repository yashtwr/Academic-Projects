var btnpi = document.getElementById("btnpi");
var btnedu = document.getElementById("btnedu");
var btnexp = document.getElementById("btnexp");

var divpi = document.getElementById("divpi");
var divedu = document.getElementById("divedu");
var divexp = document.getElementById("divexp");

divedu.style.display = "none";
btnpi.style.backgroundColor = "#fdd54f";

function openPI(){
	btnpi.style.backgroundColor = "#fdd54f";
	btnedu.style.backgroundColor = "#eee";
	btnexp.style.backgroundColor = "#eee";
	divpi.style.display = "block";
	divedu.style.display = "none";
	divexp.style.display = "none";
}
function openEdu(){
	btnedu.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#eee";
	btnexp.style.backgroundColor = "#eee";
	divedu.style.display = "block";
	divpi.style.display = "none";
	divexp.style.display = "none";
}

function openExp(){
	btnexp.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#eee";
	btnedu.style.backgroundColor = "#eee";
	divexp.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
}