from project import db
from project.com.vo.SkillsVO import SkillsVO

class SkillsDAO:
    def insertSkills(self, skillsVO):
        db.session.add(skillsVO)
        db.session.commit()

    def fetchSkills(self, id):
        skills_list = SkillsVO.query.all(skills_loginId = id)
        return skills_list