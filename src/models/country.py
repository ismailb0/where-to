from .abc import BaseModel, MetaBaseModel, db


class Country(db.Model, BaseModel, metaclass=MetaBaseModel):
    """Model class for country."""

    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    def __init__(self, name):
        """Create a new country."""
        self.name = name
