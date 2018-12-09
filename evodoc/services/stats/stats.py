from evodoc.models.user import User
from evodoc.models.package import Package
from evodoc.models.project import Project


def get_stats():
    users = User.query.get_all().count()
    packages = Package.query.get_all().count()
    projects = Project.query.get_all().count()

    return {
        'users': users,
        'packages': packages,
        'projects': projects,
    }
