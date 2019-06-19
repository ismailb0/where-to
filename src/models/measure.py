from .abc import BaseModel, MetaBaseModel, db


class Measure(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Model class for measure."""

    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    country_id = db.Column(db.Integer,
                           db.ForeignKey('country.id', ondelete='CASCADE'),
                           nullable=False)
    type = db.Column(db.String(32), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.Integer, nullable=False)

    def __init__(self, country_id, type, value, date):
        """Create a new measure."""

        self.country_id = country_id
        self.type = type
        self.value = value
        self.date = date
