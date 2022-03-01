from project import db
from project.com.vo.EducationVO import EducationVO

class EducationDAO:
    def insertEdu(self, educationVO):
        db.session.add(educationVO)
        db.session.commit()

    def fetchEdu(self, id):
        edu_list = EducationVO.query.all(education_loginId = id)
        return edu_list