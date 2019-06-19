import requests
from flask_script import Command
from bs4 import BeautifulSoup
from repositories import CountryRepository


class ImportCountries(Command):
    """Import countries from a scrapped website."""

    def __init__(self):
        self._URL = "WEBSITE_TO_GET_COUNTRIES_FROM"

    def run(self):
        print('Importing countries...')
        country_names_list = self._get_country_name_list()

        for country_name in country_names_list:
            country_repository = CountryRepository()
            country_repository.create(country_name)

        print('{} countries successfully imported'.format(len(country_names_list)))


    def _get_country_name_list(self):
        """ Get country names list from website """
        page = requests.get(self._URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        list_of_data_to_scrap = soup.find_all('font', size=-2)
        return [
            data.get_text().replace(" ", "_").replace(".", "")
            for data in list_of_data_to_scrap
            if "<a" not in str(data)
        ]
