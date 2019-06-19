from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from commands import ImportCountries, ImportMeasures
import config
from models import db

server = Flask(__name__)
server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
db.init_app(server)

migrate = Migrate(server, db)
manager = Manager(server)
manager.add_command("db", MigrateCommand)
manager.add_command('import-countries', ImportCountries)
manager.add_command('import-measures', ImportMeasures)

if __name__ == "__main__":
    manager.run()
