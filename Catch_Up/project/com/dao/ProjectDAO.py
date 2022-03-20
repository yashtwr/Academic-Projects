from project import db
from project.com.vo.ProjectVO import ProjectVO

class ProjectDAO:
    def insertProject(self, projectVO):
        db.session.add(projectVO)
        db.session.commit()

    def fetchProjects(self, projectVO):
        projects_list = ProjectVO.query.filter_by(project_loginId = projectVO.project_loginId).all()
        return projects_list
