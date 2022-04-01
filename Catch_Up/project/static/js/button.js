	function edit_row(no) {
    	
        // document.getElementById("edit_button" + no).style.display = "none";
        
        //document.getElementById("edit_button" + no).style.display = "none";
        //document.getElementById("save_button" + no).style.display = "block";
        
        var platform = document.getElementById("platform"+no);
        var link = document.getElementById("link"+no);


        var platform_data = platform.innerHTML;
        var link_data = link.innerHTML;

        platform.innerHTML = "<input type='text' width='50' id='platform_data" + no + "' value='" + platform_data + "'>";
        link.innerHTML="<input type='text' width='50' id='link_data" + no + "' value='" + link_data + "'>";
        document.getElementById("edit_button" + no).style.display = "none";
    }

    function save_row(no) {
    	
        var platform = document.getElementById("platform_data"+no).value;
        
        var link = document.getElementById("link_data" + no).value;
        
        
        document.getElementById("platform" + no).innerHTML = platform;
        document.getElementById("link" + no).innerHTML = link;

        document.getElementById("la").method = "POST"

        document.getElementById("la").action = "/updateAccounts?Id="+no+"&platform"+no+"="+platform+"&link"+no+"="+link

		document.getElementById("la").submit();
    }
    function edit_row_hobbies(no) {
    	
        // document.getElementById("edit_button" + no).style.display = "none";
        
        //document.getElementById("edit_button" + no).style.display = "none";
        //document.getElementById("save_button" + no).style.display = "block";
        
        var hobbies = document.getElementById("hobbies"+no);
        var hobbies_data = hobbies.innerHTML;
        
        hobbies.innerHTML = "<input type='text' width='50' id='hobbies_data" + no + "' value='" + hobbies_data + "'>";
        // document.getElementById("edit_button" + no).style.display = "none";
    }

    function save_row_hobbies(no) {
    	var hobbies = document.getElementById("hobbies_data"+no).value;
        document.getElementById("hobbies" + no).innerHTML = hobbies;
        document.getElementById("skills").method = "POST"

        document.getElementById("skills").action = "/updateHobbies?Id="+no+"&hobbies="+hobbies

		document.getElementById("skills").submit();
    }

    function edit_row_certi(no) {
    	
        // document.getElementById("edit_button" + no).style.display = "none";
        
        //document.getElementById("edit_button" + no).style.display = "none";
        //document.getElementById("save_button" + no).style.display = "block";
        
        var certificate = document.getElementById("certificate"+no);
        var certificate_data = certificate.innerHTML;
        

        certificate.innerHTML = "<input type='text' width='50' id='certificate_data" + no + "' value='" + certificate_data + "'>";
        // document.getElementById("edit_button" + no).style.display = "none";
    }

    function save_row_certi(no) {
    	var certificate = document.getElementById("certificate_data"+no).value;
        document.getElementById("certificate" + no).innerHTML = certificate;
        
        document.getElementById("skills").method = "POST"

        document.getElementById("skills").action = "/updateCertificates?Id="+no+"&certificates="+certificate

		document.getElementById("skills").submit();
    }
    function edit_row_project(no) {
    	
        // document.getElementById("edit_button" + no).style.display = "none";
        
        //document.getElementById("edit_button" + no).style.display = "none";
        //document.getElementById("save_button" + no).style.display = "block";
        
        var project_title = document.getElementById("project_title"+no);
        var project_detail = document.getElementById("project_detail"+no);

        var project_title_data = project_title.innerHTML;
        var project_detail_data = project_detail.innerHTML;

        project_title.innerHTML = "<input type='text' width='50' id='project_title_data" + no + "' value='" + project_title_data + "'>";
        project_detail.innerHTML="<input type='text' width='50' id='project_detail_data" + no + "' value='" + project_detail_data + "'>";
        
        // document.getElementById("edit_button" + no).style.display = "none";
    }

    function save_row_project(no) {
        var project_title = document.getElementById("project_title_data"+no).value;
        var project_detail = document.getElementById("project_detail_data" + no).value;
        document.getElementById("project_title" + no).innerHTML = project_title;
        document.getElementById("project_detail" + no).innerHTML = project_detail;
        document.getElementById("skills").method = "POST"

        document.getElementById("skills").action = "/updateProject?Id="+no+"&project_title="+project_title+"&project_detail="+project_detail

		document.getElementById("skills").submit();
    }

	function edit_row_course(no) {
    	
        // document.getElementById("edit_button" + no).style.display = "none";
        
        //document.getElementById("edit_button" + no).style.display = "none";
        //document.getElementById("save_button" + no).style.display = "block";
        var department = document.getElementById("department"+no);
        var course_no = document.getElementById("course_no"+no);
        

        var department_data = department.innerHTML;
        var course_no_data = course_no.innerHTML;
        
        department.innerHTML = "<input type='text' width='50' id='department_data" + no + "' value='" + department_data + "'>";
        course_no.innerHTML="<input type='text' width='50' id='course_no_data" + no + "' value='" + course_no_data + "'>";
        // document.getElementById("edit_button" + no).style.display = "none";
    }

    function save_row_course(no) {
    	
        var course_no = document.getElementById("course_no_data"+no).value;
        
        var department = document.getElementById("department_data" + no).value;
        
        
        document.getElementById("course_no" + no).innerHTML = course_no;
        document.getElementById("department" + no).innerHTML = department;

        document.getElementById("edu").method = "POST"

        document.getElementById("edu").action = "/updateCourse?Id="+no+"&course_no="+course_no+"&department="+department

		document.getElementById("edu").submit();
    }

