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

btnpi.addEventListener("mouseover", mouseOver);
btnpi.addEventListener("mouseout", mouseOut);

function mouseOver(event){
	btnpi.style.backgroundColor = "#fdd54f";
	btnpi.style.color="#000";
}
function mouseOut(event){
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
}

divedu.style.display = "none";
divexp.style.display = "none";
divskills.style.display = "none";
divla.style.display = "none";
divpi.style.display = "block";

if (divpi.style.display == "block"){
	btnpi.style.color = "#000";
	btnpi.style.backgroundColor = "#fdd54f";
}

function openPI(){
	btnpi.style.backgroundColor = "#fdd54f";
	btnpi.style.color="#000";
	btnpi.removeEventListener("mouseout", changeStyle1);
	
	divpi.style.display = "block";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}
function openEdu(){
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
	btnpi.addEventListener("mouseout", changeStyle1);
	
	divedu.style.display = "block";
	divpi.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}

function openExp(){
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
	btnpi.addEventListener("mouseout", changeStyle1);
	
	divexp.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}

function openSkills(){
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
	btnpi.addEventListener("mouseout", changeStyle1);
	
	divskills.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divla.style.display = "none";
}

function openLA(){
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
	btnpi.addEventListener("mouseout", changeStyle1);
	
	divla.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
}
