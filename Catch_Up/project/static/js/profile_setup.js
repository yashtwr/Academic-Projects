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

/*btnpi.style.color = "#000";

btnpi.style.backgroundColor = "#fdd54f";
btnedu.style.backgroundColor = "#000";
btnexp.style.backgroundColor = "#000";
btnskills.style.backgroundColor = "#000";
btnla.style.backgroundColor = "#000";*/

function openPI(){
	/*btnpi.style.backgroundColor = "#fdd54f";
	btnedu.style.backgroundColor = "#000";
	btnexp.style.backgroundColor = "#000";
	btnskills.style.backgroundColor = "#000";
	btnla.style.backgroundColor = "#000";
	
	btnpi.style.color="#000";
	btnedu.style.color="#fdd54f";
	btnexp.style.color="#fdd54f";
	btnskills.style.color="#fdd54f";
	btnla.style.color="#fdd54f";*/
	
	divpi.style.display = "block";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}
function openEdu(){
	/*btnedu.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#000";
	btnexp.style.backgroundColor = "#000";
	btnskills.style.backgroundColor = "#000";
	btnla.style.backgroundColor = "#000";
	
	btnedu.style.color="#000";
	btnpi.style.color="#fdd54f";
	btnexp.style.color="#fdd54f";
	btnskills.style.color="#fdd54f";
	btnla.style.color="#fdd54f";*/
	
	
	divedu.style.display = "block";
	divpi.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}

function openExp(){
	/*btnexp.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#000";
	btnedu.style.backgroundColor = "#000";
	btnskills.style.backgroundColor = "#000";
	btnla.style.backgroundColor = "#000";
	
	btnexp.style.color="#000";
	btnpi.style.color="#fdd54f";
	btnedu.style.color="#fdd54f";
	btnskills.style.color="#fdd54f";
	btnla.style.color="#fdd54f";*/
	
	divexp.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}

function openSkills(){
	/*btnskills.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#000";
	btnedu.style.backgroundColor = "#000";
	btnexp.style.backgroundColor = "#000";
	btnla.style.backgroundColor = "#000";
	
	btnskills.style.color="#000";
	btnpi.style.color="#fdd54f";
	btnedu.style.color="#fdd54f";
	btnexp.style.color="#fdd54f";
	btnla.style.color="#fdd54f";*/
	
	divskills.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divla.style.display = "none";
}

function openLA(){
	/*btnla.style.backgroundColor = "#fdd54f";
	btnpi.style.backgroundColor = "#000";
	btnedu.style.backgroundColor = "#000";
	btnexp.style.backgroundColor = "#000";
	btnskills.style.backgroundColor = "#000";
	
	btnla.style.color="#000";
	btnpi.style.color="#fdd54f";
	btnedu.style.color="#fdd54f";
	btnexp.style.color="#fdd54f";
	btnskills.style.color="#fdd54f";*/
	
	divla.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
}
