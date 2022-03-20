from project import db
from project.com.vo.CoursesVO import CoursesVO

class CoursesDAO:
    def insertCourses(self, coursesVO):
        db.session.add(coursesVO)
        db.session.commit()

    def fetchCourses(self, coursesVO):
        courses_list = CoursesVO.query.filter_by(course_loginId = coursesVO.course_loginId).all()
        return courses_list
