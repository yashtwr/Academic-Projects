var btnpi = document.getElementById("btnpi");
var btnedu = document.getElementById("btnedu");
var btnexp = document.getElementById("btnexp");
var btnskills = document.getElementById("btnskills");
var btnla = document.getElementById("btnla");

var divpi = document.getElementById("divpi");
var divedu = document.getElementById("divedu");
var divexp = document.getElementById("divexp");
var divskills = document.getElementById("divskills");
var divla = document.getElementById("divla");

divedu.style.display = "none";
divexp.style.display = "none";
divskills.style.display = "none";
divla.style.display = "none";
btnpi.style.backgroundColor = "#fdd54f";
btnedu.style.backgroundColor = "#eee";
btnexp.style.backgroundColor = "#eee";
btnskills.style.backgroundColor = "#eee";
btnla.style.backgroundColor = "#eee";

function openPI(){
	btnpi.style.backgroundColor = "#fdd54f";
	btnedu.style.backgroundColor = "#eee";
	btnexp.style.backgroundColor = "#eee";
	btnskills.style.backgroundColor = "#eee";
	btnla.style.backgroundColor = "#eee";
	
	divpi.style.display = "block";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}
function openEdu(){
	btnedu.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#eee";
	btnexp.style.backgroundColor = "#eee";
	btnskills.style.backgroundColor = "#eee";
	btnla.style.backgroundColor = "#eee";
	
	divedu.style.display = "block";
	divpi.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}

function openExp(){
	btnexp.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#eee";
	btnedu.style.backgroundColor = "#eee";
	btnskills.style.backgroundColor = "#eee";
	btnla.style.backgroundColor = "#eee";
	
	divexp.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}

function openSkills(){
	btnskills.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#eee";
	btnedu.style.backgroundColor = "#eee";
	btnexp.style.backgroundColor = "#eee";
	btnla.style.backgroundColor = "#eee";
	
	divskills.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divla.style.display = "none";
}

function openLA(){
	btnla.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#eee";
	btnedu.style.backgroundColor = "#eee";
	btnexp.style.backgroundColor = "#eee";
	btnskills.style.backgroundColor = "#eee";
	
	divla.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
}
