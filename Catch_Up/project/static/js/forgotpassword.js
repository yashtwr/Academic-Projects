var myInput = document.getElementById("newpswd");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
  document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
  document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {  
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }
  
  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {  
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {  
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }
  
  // Validate length
  if(myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}

function validateForm() {
	
	var un = document.forms["forgotpswdform"]["username"].value;
	var newp = document.forms["forgotpswdform"]["newpswd"].value;
	var cp = document.forms["forgotpswdform"]["confirmpswd"].value;
	
	var small = /[a-z]/.test(newp);
	var capital = /[A-Z]/.test(newp);
	var num = /[0-9]/.test(newp);

	if (newp.length < 8){
		alert("Password must contain at least 8 characters");
		document.forms["forgotpswdform"]["newpswd"].focus();
		document.forms["forgotpswdform"]["newpswd"].select();
		return false;
	}
	
	else if (!(small && capital && num)){
		alert("Please fill all the details of Password");
		document.forms["forgotpswdform"]["newpswd"].focus();
		document.forms["forgotpswdform"]["newpswd"].select();
		return false;
	}
	
	else if(newp!=cp){
		alert("Both password should be same");
		document.forms["forgotpswdform"]["confirmpswd"].focus();
		document.forms["forgotpswdform"]["confirmpswd"].select();
		return false;
	}
	
	else{
		return true;
	}
}
function resetfun(){
	document.getElementById("usr").focus();
	//document.forms["forgotpswdform"]["username"].focus();
}
