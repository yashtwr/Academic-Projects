from project import db
from project.com.vo.ProjectVO import ProjectVO

class ProjectDAO:
    def insertProject(self, projectVO):
        db.session.add(projectVO)
        db.session.commit()

    def fetchProjects(self, id):
        projects_list = ProjectVO.query.all(project_loginId = id)
        return projects_list