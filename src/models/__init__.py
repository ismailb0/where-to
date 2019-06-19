from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .country import Country
from .measure import Measure
