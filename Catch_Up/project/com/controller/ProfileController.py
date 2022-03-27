{% extends "profile_setup_layout.html" %}
{% block content %}

<link rel="stylesheet" href = "../static/css/profile_setup.css">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <div class = "profile">
	<h1 id="title">Profile</h1>
	<div class = "btn-box">
		<button id="btnpi" onclick="openPI()"> Personal Information </button>
		<button id="btnedu" onclick="openEdu()"> Education </button>
		<button id="btnexp" onclick="openExp()"> Experience </button>
		<button id="btnskills" onclick="openSkills()"> Skills </button>
		<button id="btnla" onclick="openLA()"> Linked Account </button>
	</div>

	<div id="divpi" class="content">
	  <form class="pi" >
		<div class="form-group same" id="fnamediv">	
			<label for="first" class="same" id="fnamelabel">First Name:</label>	
			{% if signup %}
			<input type="text" class="form-control same" id="firstname" name="firstname" value="{{signup[0]['firstname']}}">	
			{% else %}
			<input type="text" class="form-control same" id="firstname" name="firstname" >	
			{% endif %}
		</div>	
		<div class="form-group same" id="lnamediv">	
			<label for="last" class="same" id="lnamelabel">Last Name:</label>	
			
			{% if signup %}
			<input type="text" class="form-control same" id="lastname" name="lastname" value="{{signup[0]['lastname']}}">
			{% else %}
			<input type="text" class="form-control same" id="lastname" name="lastname">
			{% endif %}
		</div>	
		<div class="form-group same" id="emaildiv">	
			<label for="email" class="same" id="emaillabel">Email:</label>	
				
			{% if personal %}
			<input type="email" pattern="[a-zA-Z0-9.-_]{1,}@[a-zA-Z.-]{2,}[.]{1}[a-zA-Z]{2,}" class="form-control same" placeholder="Enter Email" id="contact_email" name="contact_email" value="{{personal[0]['contact_email']}}">
			{% else %}
			<input type="email" pattern="[a-zA-Z0-9.-_]{1,}@[a-zA-Z.-]{2,}[.]{1}[a-zA-Z]{2,}" class="form-control same" placeholder="Enter Email" id="contact_email" name="contact_email">
			{% endif %}
		</div>
		<div class="form-group same" id="contactdiv">	
			<label for="contactno" class="same" id="contactlabel">Contact No:</label>	
				
			{% if personal %}
			<input type="text" pattern="[0-9]{10}" class="form-control same" id="contact_number" name="contact_number" value="{{personal[0]['contact_number']}}">
			{% else %}
			<input type="text" pattern="[0-9]{10}" class="form-control same" id="contact_number" name="contact_number">
			{% endif %}
		</div>
		<div class="form-group same" id="addressdiv">	
			<label for="address" class="same" id="addresslabel">Address:</label>	

			{% if personal %}
			<input type="text" class="form-control same" id="address" name="address" value="{{personal[0]['address']}}">	
			{% else %}
			<input type="text" class="form-control same" id="address" name="address">	
			{% endif %}
			
		</div>

		<div class="form-group same" id="description">	
			<label for="first" class="same" id="description">Description:</label>	
			
			{% if personal %}
			<input type="text" class="form-control same" id="description" name="description" value="{{personal[0]['description']}}">	
			{% else %}
			<input type="text" class="form-control same" id="description" name="description">	
			{% endif %}
			
		</div>	

			{% if personal %}
				<input type="hidden" id="Id" name="Id" value="{{personal[0]['Id']}}">
			{% else %}
				<input type="hidden" id="Id" name="Id" value="Null">
			{% endif %}
		<button type= "submit" formaction="insertPersonalInfo" style="background-color:black; color:#fdd54f; border-width:0; margin: 0px 0px 10px 15px;" formmethod="POST">Update</button>
	  </form>
	</div>
	


	<div id="divedu" class="content">
	  <form class="edu">

		<div class="form-group same" >
			<label for="last" class="same" id="degree_name">Department:</label>
			{% if courses%}
			<input type="text" class="form-control same" id="department" name="department" value="{{courses[0]['department']}}">
			{%else%}
			<input type="text" class="form-control same" id="department" name="department">

			{%endif%}
		</div>

		<!-- add and delete courses-->
		    <!-- add and delete courses-->
        <div class="form-group same" style="margin: 0px;">
            <label for="first" class="same">Course No.:</label>
            {% for course in courses %}

            <input type="text" class="form-control same" id="{{course['Id']}}" name="course_no{{course['Id']}}"
                   value="{{ course['course_no'] }}"/>
            <a class= "material-icons md-40 md-dark" href="deleteCourse?courseid={{course['course_no']}}" style="color:black; background-color: transparent; text-decoration: none;">delete</a>
            <button type= "submit" formaction="updateCourse?Id={{course['Id']}}" style="background-color:#fdd54f; margin:10px 0px; border-width:0;" formmethod="POST"><i style="background-color:#fdd54f" class= "material-icons md-36">edit</i></button>
            {% endfor %}
            <input type="text" class="form-control same" id="course_no1" name="courseno">
            <button type="submit" formaction="insertCourse" formmethod="POST" style="background-color:#fdd54f; margin:10px 0px; border-width:0;"><i class="material-icons md-48 md-dark">add_circle</i></button>

        </div>


		<div class="form-group same" id="degree_name">
			<label for="last" class="same" id="degree_name">Degree:</label>
			{% if education %}
			<input type="text" class="form-control same" id="degree_name" name="degree_name" value="{{education[0]['degree_name']}}">
			{% else %}
			<input type="text" class="form-control same" id="degree_name" name="degree_name">
			{% endif %}
		</div>

		<div class="form-group same" id="institution_name">
			<label for="first" class="same" id="institution_name">Institution name:</label>
			{% if education %}
			<input type="text" class="form-control same" id="institution_name" name="institution_name" value="{{education[0]['institution_name']}}">
			{% else %}
			<input type="text" class="form-control same" id="institution_name" name="institution_name">
			{% endif %}
		</div>

		<div class="form-group same" id="start_date">
			<label for="last" class="same" id="start_date">Start Year:</label>

			{% if education %}
			<input type="text" class="form-control same" id="start_date" name="start_date" value="{{education[0]['start_date']}}">
			{% else %}
			<input type="text" class="form-control same" id="start_date" name="start_date">
			{% endif %}
		</div>

		<div class="form-group same" id="end_date">
			<label for="first" class="same" id="end_date">End Year:</label>

			{% if education %}
			<input type="text" class="form-control same" id="end_date" name="end_date" value="{{education[0]['end_date']}}">
			{% else %}
			<input type="text" class="form-control same" id="end_date" name="end_date">
			{% endif %}
		</div>

		<div class="form-group same" id="cgpa">
			<label for="first" class="same" id="cgpa">CGPA:</label>
			{% if education %}
			<input type="number" min="0" step=".01" class="form-control same" id="cgpa" name="cgpa" value="{{education[0]['cgpa']}}">
			{% else %}
			<input type="number" min="0" value="0" step=".01" class="form-control same" id="cgpa" name="cgpa">
			{% endif %}

		</div>
		{% if education %}
			<input type="hidden" id="Id" name="Id" value="{{education[0]['Id']}}">
		{% else %}
			<input type="hidden" id="Id" name="Id" value="Null">
		{% endif %}
		<button type="submit" formaction="insertEducation" formmethod="POST" style="background-color:black; color:#fdd54f; margin: 0px 0px 10px 20px;">Update</button>

	  </form>
	</div>

	<div id="divexp" class="content">
	  <form class="exp" method="post" action="/insertIndustryExp">
		<div class="form-group same">
			<label for="first" class="same">Company Name:</label>
			{% if industryExp %}
				<input type="text" class="form-control same" id="company_name" name="company_name" value="{{industryExp[0]['company_name']}}">
			{% else %}
				<input type="text" class="form-control same" id="company_name" name="company_name">
			{% endif %}
		</div>

		<div class="form-group same">
			<label for="first" class="same">Designation:</label>
			{% if industryExp %}
				<input type="text" class="form-control same" id="designation" name="designation" value="{{industryExp[0]['designation']}}">
			{% else %}
				<input type="text" class="form-control same" id="designation" name="designation" >
			{%endif%}
		</div>

		<div class="form-group same" >
			<label for="first" class="same" >Work Description:</label>
			{% if industryExp %}
				<input type="text" class="form-control same" id="work_description" name="work_description" value="{{industryExp[0]['work_description']}}">
			{%else%}
				<input type="text" class="form-control same" id="work_description" name="work_description">
			{%endif%}
		</div>

		<div class="form-group same" >
			<label for="first" class="same">No. of Months:</label>
			{% if industryExp %}
				<input type="number" min="1" class="form-control same" id="no_of_months" name="no_of_months" value="{{industryExp[0]['no_of_months']}}">

				<input type="hidden" id="Id" name="Id" value="{{industryExp[0]['Id']}}">
			{% else %}
				<input type="number" min="1" class="form-control same" id="no_of_months" name="no_of_months">
				<input type="hidden" id="Id" name="Id" value="Null">
			{% endif %}
		</div>

        {% if industryExp %}
          <button type="submit" formaction="insertIndustryExp" formmethod="post" style="background-color:#fdd54f; border-width:0; margin: 0px 0px 5px 10px;"><i style="background-color:#fdd54f;" class="material-icons md-48 md-dark">edit</i></button>
          <button type="submit" formaction="deleteIndustryExp?Id={{industryExp['Id']}}" formmethod="GET" style="background-color:#fdd54f; border-width:0; "><i style="background-color:#fdd54f;" class="material-icons md-48 md-dark">delete</i></button>
          <!--<button type="submit" formaction="deleteIndustryExp?Id={{industryExp['Id']}}" formmethod="GET"><i class="material-icons md-48 md-dark">delete</i></button>-->
          {%else%}
          <button type="submit" formaction="insertIndustryExp" formmethod="post" style="background-color:#fdd54f; border-width:0; margin: 0px 0px 5px 10px;"><i style="background-color:#fdd54f;" class="material-icons md-48 md-dark">add_circle</i></button>
          {%endif%}
	  </form>
	</div>

	<div id="divskills" class="content">
	  <form class="skills">

		<div class="form-group same" style="margin:5px 0px 0px 0px;">
			<label for="first" class="same" >Certificates:</label>
			{% for certificate in certificates %}

			  <input type="text" class="form-control same" id="{{certificate['Id']}}" name="certificate{{certificate['Id']}}" value="{{ certificate['certificates'] }}">
		      <a class= "material-icons md-48 md-dark" href="deleteCertificates?Id={{certificate['Id']}}" style="color:black; background-color: transparent; text-decoration: none;">delete</a>
                <button type= "submit" formaction="updateCertificates?Id={{certificate['Id']}}" style="background-color:#fdd54f; border-width:0; margin: 10px 0px;" formmethod="POST"><i style="background-color:#fdd54f" class= "material-icons md-48 md-dark">edit</i></button>
		      {% endfor %}

            <input type="text" class="form-control same" id="certificate" name="certificates">
            <button name="insertCertificates" formaction="insertCertificates" formmethod="post" style="background-color:#fdd54f; border-width:0; margin: 10px 0px;"><i style="background-color:#fdd54f;" class="material-icons md-48 md-dark">add_circle</i></button>
		</div>

		<div class="form-group same" id="project_title">
			<label for="first" class="same" id="project_title">Project Title:</label>
			{% for project in projects %}
			<input type="text" class="form-control same" id="{{project['Id']}}" name="project_title{{project['Id']}}" value="{{ project['project_title'] }}">
		    {% endfor %}
			<input type="text" class="form-control same" id="project_title" name="project_title">
		</div>

		<div class="form-group same" id="project_detail">
			<label for="first" class="same" id="project_detail">Project Detail:</label>
			{% for project in projects %}

			  <input type="text" class="form-control same" id="{{project['Id']}}" name="project_detail{{project['Id']}}" value="{{ project['project_detail'] }}">
		      <a class= "material-icons md-48 md-dark same" href="deleteProject?Id={{project['Id']}}" style="color:black; background-color: transparent; text-decoration: none;">delete</a>
                <button type= "submit" formaction="updateProject?Id={{project['Id']}}" style="background-color:#fdd54f; margin:10px 0px; border-width:0px;" formmethod="POST"><i style="background-color:#fdd54f" class= "material-icons md-48 md-dark same">edit</i></button>
		    {% endfor %}

			<input type="text" class="form-control same" id="project_detail" name="project_detail">
			<button type="submit" formaction="insertProject" formmethod="POST" style="background-color:#fdd54f; border-width:0; margin: 10px 0px;"><i style="background-color:#fdd54f;" class="material-icons md-48 md-dark">add_circle</i></button>
		</div>
		<div class="form-group same" id="project_detail">
			<label for="first" class="same" id="project_detail">Hobbies:</label>
			{% for h in hobbies %}
			  <input type="text" class="form-control same" id="{{h['Id']}}" name="hobbies{{h['Id']}}" value="{{ h['hobbies'] }}">
		      <a class= "material-icons md-48 md-dark same" href="deleteHobbies?Id={{h['Id']}}" style="color:black; background-color: transparent; text-decoration: none;">delete</a>
                <button type= "submit" formaction="updateHobbies?Id={{h['Id']}}" style="background-color:#fdd54f; margin:10px 0px; border-width:0px;" formmethod="POST"><i style="background-color:#fdd54f" class= "material-icons md-48 md-dark same">edit</i></button>
		    {% endfor %}

			<input type="text" class="form-control same" id="hobbies" name="hobbies">
			<button type="submit" formaction="insertHobbies" formmethod="POST" style="background-color:#fdd54f; margin:10px 0px; border-width:0px;"><i style="background-color:#fdd54f" class= "material-icons md-48 md-dark same">edit</i></button>
		</div>



	  </form>
	</div>
	
	<div id="divla" class="content">
	  <form class="la">

        {% for account in accounts %}
        <div class="form-group same" id="other_links" style="margin: 5px 0px 0px 0px;">
            <label for="first" class="same" id="linkedIn_account">Platform:</label>
            <input type="text" class="form-control same" id="linkedIn_account" name="platform{{account['Id']}}" value = "{{account['platform']}}">
            <label for="first" class="same"  style="margin: 10px 0px;">Link:</label>
            <input type="text" class="form-control same" id="{{['Id']}}" name="link{{account['Id']}}"
                   value="{{ account['link'] }}">
            <a class= "material-icons md-40 md-dark" href="deleteAccounts?Id={{account['Id']}}" style="color:black; background-color: transparent; text-decoration: none;">delete</a>
            <button type= "submit" formaction="updateAccounts?Id={{account['Id']}}" style="background-color:#fdd54f; border-width:0; margin: 10px 0px;" formmethod="POST"><i style="background-color:#fdd54f" class= "material-icons md-36">edit</i></button>
        </div>
        {% endfor %}
        <div class="form-group same" id="other_links" style="margin: 0px;">
            <label for="first" class="same" id="linkedIn_account">Platform:</label>
            <input type="text" class="form-control same" id="linkedIn_account" name="platform">
            <label for="first" class="same" id="linkedIn_account" style="margin: 10px 0px;">Link:</label>
            <input type="text" class="form-control same" id="course_no1" name="link">
            <button type="submit" formaction="insertAccount" formmethod="POST" style="background-color:#fdd54f; border-width:0; margin: 10px 0px;"><i style="background-color:#fdd54f;" class="material-icons md-48 md-dark">add_circle</i></button>
        </div>


	  </form>
	</div>
	
</div>
</form>

<script src = "../static/js/profile_setup.js"></script>
{%if session['currentPage']=='personal_information' %}
<script> openPI();console.log("this is printed");</script>

{%elif session['currentPage']=='education' %}
<script>openEdu();console.log("this is printed");</script>
{%elif session['currentPage']== 'experience'%}
<script>openExp();console.log("this is printed");</script>
{%elif session['currentPage']== 'skills' %}
<script>openSkills();console.log("this is printed");</script>
{%else%}
<script>openLA();console.log("this is printed");</script>
{%endif%}

{% endblock content %}
