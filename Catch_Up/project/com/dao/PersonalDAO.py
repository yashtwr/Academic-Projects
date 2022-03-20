from project import db
from project.com.vo.PersonalVO import PersonalVO

class PersonalDAO:
    def insertPersonal(self, personalVO):
        db.session.add(personalVO)
        db.session.commit()

    def fetchPersonal(self, personalVO):
        personal_list = PersonalVO.query.filter_by(personal_loginId = personalVO.personal_loginId).all()
        return personal_list
