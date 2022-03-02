from project import db
from project.com.vo.PersonalVO import PersonalVO

class PersonalDAO:
    def insertPersonal(self, personalVO):
        db.session.add(personalVO)
        db.session.commit()

    def fetchPersonal(self, id):
        personal_list = PersonalVO.query.all(personal_loginId = id)
        return personal_list