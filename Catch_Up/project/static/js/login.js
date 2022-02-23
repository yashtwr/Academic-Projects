function validateForm() {
	
	var un = document.forms["login"]["username"].value;
	var pswd = document.forms["login"]["password"].value;

	if (un == "") {
		alert("Username cannot be empty");
		document.forms["login"]["username"].focus();
		return false;
	}
	
	else if (pswd == "") {
		alert("Password cannot be empty");
		document.forms["login"]["password"].focus();
		return false;
	}
	
}