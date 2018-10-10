from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__, instance_relative_config=True)

import sys
sys.path.append("./")

#Configuration load, this is maybe just temporary solution
app.config.from_object('evodoc.conf')

from evodoc.models import db
migrate = Migrate(app, db, render_as_batch=True)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
