from project import db
from project.com.vo.EducationVO import EducationVO

class EducationDAO:
    def insertEducation(self, educationVO):
        db.session.add(educationVO)
        db.session.commit()

    def fetchEducation(self, educationVO):
        edu_list = EducationVO.query.filter_by(education_loginId = educationVO.education_loginId).all()
        return edu_list
