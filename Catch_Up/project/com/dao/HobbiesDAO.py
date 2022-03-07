from project import db
from project.com.vo.HobbiesVO import HobbiesVO

class HobbiesDAO:
    def insertHobbies(self, hobbiesVO):
        db.session.add(hobbiesVO)
        db.session.commit()

    def fetchHobbies(self, id):
        hobbies_list = HobbiesVO.query.all(hobbies_loginId = id)
        return hobbies_list