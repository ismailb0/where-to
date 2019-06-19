""" Defines the country repository """

from models import Country


class CountryRepository:
    """ The repository for the country model """

    @staticmethod
    def get_all():
        """ Query all countries """
        return Country.query.all()

    @staticmethod
    def create(country_name):
        """ Create a new country """
        country = Country(country_name)

        return country.save()
