from evodoc.models import Module, Project
# from flask import g
from evodoc.exception import ApiException
import pypandoc
import evodoc.conf as conf
import pathlib


def gatherModule(g, currentModule, visitedModules=[]):
    """
    Recursively builds module
        :param g: context
        :param currentModule: module name
        :param visitedModules=[]: list of visited modules
    """
    out = ''
    visitedModules.append(currentModule)
    module = Module.query.filter_by(project_id=g.project.id,
                                    name=currentModule).first()
    if module is None:
        raise ApiException(500, 'Build error.', visitedModules)

    content = ''
    with open(conf.FILE_PATH +
              '/' +
              str(g.project.id) +
              '/' +
              str(module.id) +
              '.txt', 'r') as f:
        content = f.read()

    content = pypandoc.convert_text(
        content,
        'html',
        format=module.contentType)

    content = content.split(conf.TAG)

    for x in range(0, len(content)):
        if x % 2 == 0:
            out += content[x]
        else:
            out += gatherModule(g, content[x], visitedModules)

    return out


def build(g):
    """
    Builds pdf from module and adds the path to product to context (g)
        :param g: context
    """
    g.module = Module.query.get_active(g.id)
    if g.module is None:
        raise ApiException(
            404,
            "Module not found.",
            ['module'])

    g.project = Project.query.get_active(g.module.project_id)
    if g.project is None:
        raise ApiException(
            404,
            "Project not found.",
            ['project'])

    if g.project.owner_id != g.token.user_id:
        contributor = 0
        for user in g.project.contributors:
            if user.id == g.token.user_id:
                contributor = 1
                break
        if contributor == 0:
            raise ApiException(
                403,
                "Access denied (no rights)",
                ['project'])

    path = (conf.FILE_PATH +
            '/' +
            str(g.project.id) +
            '/' +
            str(g.module.id) +
            '/')

    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    content = gatherModule(g, g.module.name)

    g.pdf = path+'out.pdf'
    pypandoc.convert_text(content, 'latex', format='html',
                          outputfile=g.pdf)
