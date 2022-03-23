from project import db
from project.com.vo.CoursesVO import CoursesVO

class CoursesDAO:
	# insert into database
    def insertCourses(self, coursesVO):
        db.session.add(coursesVO)
        db.session.commit()

    # fetch records from database
    def fetchCourses(self, coursesVO):
        courses_list = CoursesVO.query.filter_by(course_loginId = coursesVO.course_loginId).all()
        return courses_list

    # delete records from database
    def deleteCourses(self, course_no, login_id):
        CoursesVO.query.filter_by(course_no=course_no, course_loginId=login_id).delete()
        db.session.commit()
