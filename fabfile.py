from fabric.api import *

env.user = 'evodoc'
env.hosts = ['dev.evodoc.hampl.space']

def pack():
    # build the package
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    # figure out the package name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = '%s.tar.gz' % dist

    # upload the package to the temporary folder on the server
    put('dist/%s' % filename, '/tmp/%s' % filename)

    # install the package in the application's virtualenv with pip
    sudo('/var/www/evodoc/venv/bin/pip install /tmp/%s' % filename)

    with shell_env(FLASK_APP='evodoc:app'):
        sudo('/var/www/evodoc/venv/bin/flask db upgrade')

    # remove the uploaded package
    run('rm -r /tmp/%s' % filename)

    sudo('sudo service supervisor restart')