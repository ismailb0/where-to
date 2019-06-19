""" Defines the measure repository """

from models import Measure


class MeasureRepository:
    """ The repository for the measure model """

    @staticmethod
    def create(
        country_id,
        measure_type,
        measure_value,
        measure_date
    ):
        """ Create a new measure """
        measure = Measure(
            country_id,
            measure_type,
            measure_value,
            measure_date
        )

        return measure.save()
