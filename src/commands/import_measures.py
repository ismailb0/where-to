import requests
from flask_script import Command
from bs4 import BeautifulSoup
from repositories import CountryRepository, MeasureRepository


class ImportMeasures(Command):
    """Import measures from a scrapped website."""

    def __init__(self):
        self._FIELDS_TO_KEEP = [
            "Tmean",
            "Tmin",
            "Tmax",
            "precip",
            "wetdays",
        ]
        self._BASE_URL = "WEBSITE_TO_GET_COUNTRIES_FROM"

    def run(self):
        measure_repository = MeasureRepository()
        print('Importing countries...')
        countries = self._get_countries()

        for country in countries:
            country_data = self._get_country_data(country.name)
            for month in country_data.keys():
                for measure_type, measure_value in country_data[month].items():
                    measure_repository.create(
                        country.id,
                        measure_type,
                        measure_value,
                        month
                    )

        print('{} measures successfully imported'.format(
            len(countries) * len(self._FIELDS_TO_KEEP) * 12
            )
        )


    def _get_country_data(self, country_name):
        """ Get weather averages for a given country """
        url = self._BASE_URL + 'data/obs.{}.htm'.format(country_name)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        list_of_data_to_scrap = soup.find_all('font', size="-1", text=True)

        data = {}

        for data_to_scrap in list_of_data_to_scrap[1:]:
            parsed_value = self._parse_values(data_to_scrap)
            if parsed_value[0] in self._FIELDS_TO_KEEP:
                measure_type = parsed_value[0]
                for index, value in enumerate(parsed_value[6:]):
                    if index + 1 in data.keys():
                        data[index + 1][measure_type] = value
                    else:
                        data[index + 1] = { measure_type: value }
        return data

    def _parse_columns(self, columns):
        """ Parse columns """
        return columns.prettify(
            formatter="html"
        ).replace("&nbsp; ", "\n").replace("&nbsp;", "").replace(" ", "").replace("\r", "").split("\n")[1:-1]

    def _parse_values(self, value_list):
        """ Parse values """
        return value_list.prettify(
            formatter="html"
        ).replace("&nbsp;", "").replace(" ", "").split("\n")[1:-1]

    def _get_countries(self):
        """ Get countries list """
        country_repository = CountryRepository()
        return country_repository.get_all()
