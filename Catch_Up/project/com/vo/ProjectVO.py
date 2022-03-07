from project import db
from project.com.vo.LoginVO import LoginVO

class ProjectVO(db.Model):
    __tablename__ = "projectsmaster"
    Id = db.Column('Id', db.Integer, primary_key=True, autoincrement=True)
    projects = db.Column('projects',db.String(20))
    description = db.Column('description',db.String(200))
    project_loginId = db.Column('project_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'Id': self.Id,
            'projects': self.projects,
            'description': self.description
        }

db.create_all()