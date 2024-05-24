from typing import Generator

import requests

from natural_loader import NPS_SERVICE_API_KEY, logger
from natural_loader.db.engine import get_db
from natural_loader.parker.constants import BASE_URL, Parameters, Resource
from natural_loader.parker.models.base_document import BaseDocument
from natural_loader.parker.models.park_data import ParkData
from natural_loader.utils.split import split


class Parker:
    def __init__(self):
        get_db()
        return

    def prepare_headers(self) -> dict[str, str]:
        """
        Takes a dictionary of headers and returns a dictionary with the API key added.
        """
        headers = {"accept": "application/json", "X-Api-Key": NPS_SERVICE_API_KEY}
        return headers

    def param_dict_to_str(self, query_parameters: Parameters) -> str:
        """
        Takes a dictionary of key value pairs. Will return the uri encoded format
        with the structure: ?key1=value1&key2=value2.
        If the value is a list, joins the values of the list with a comma.
        IE:
            {limit:1, start:1} becomes ?limit=1&start=1
        """
        target = ""
        logger.debug(f"Converting {query_parameters} to string")
        for key, value in query_parameters.items():
            if isinstance(value, list):
                value = ",".join(str(v) for v in value)
            target += f"&{key}={value}"
        return "?" + target[1:] if target else ""

    def construct_query(self, resource: Resource, query_parameters: Parameters) -> str:
        """
        Takes a Resource enum and a dictionary of query parameters.
        Returns a string that is the full query.
        """
        endpoint = resource.value
        query_string = self.param_dict_to_str(query_parameters)
        return f"{BASE_URL}{endpoint}{query_string}"

    def get_resource(
        self, resource: Resource, query_parameters: Parameters
    ) -> list[dict]:
        """
        Takes a Resource enum and a dictionary of query parameters.
        Returns an instance of the class that corresponds to that resource.
        """
        query = self.construct_query(resource, query_parameters)
        headers = self.prepare_headers()
        logger.debug(f"Making request to {query}")
        response = requests.get(query, headers=headers)
        response.raise_for_status()
        data = response.json()["data"]
        logger.debug(f"Received data. Length of {len(data)}")
        return data

    def get_resource_generator(
        self, resource: Resource, query_parameters: Parameters, limit=25
    ) -> Generator[list[dict], None, None]:
        """
        Takes a Resource enum and a dictionary of query parameters.
        Returns all instances of the class that corresponds to that resource.
        """
        query_parameters["start"] = 0
        query_parameters["limit"] = limit
        logger.debug("Starting generator")
        while True:
            data = self.get_resource(resource, query_parameters)
            if not data or len(data) < limit:
                for data in data:
                    yield data

                break
            for data in data:
                yield data
            query_parameters["start"] += query_parameters["limit"]
            logger.debug(f"Getting more data. Start is now {query_parameters['start']}")
        logger.debug("Generator finished")
        return

    def get_all_park_data(self) -> list[ParkData]:
        """
        Returns all park data from the NPS API.
        """
        query_parameters = {"start": 0}
        return [
            ParkData.from_response(data)
            for data in self.get_resource_generator(Resource.PARKS, query_parameters)
        ]

    def bulk_save(self, data: list[BaseDocument], chunk_size=25):
        """
        Takes a list of BaseDocument instances and saves them to the database.
        """
        if not data:
            return
        first_document = data[0]
        first_class = first_document.__class__
        logger.debug(f"Saving set of {first_class.__name__}")
        logger.debug(f"Saving {len(data)} documents")
        first_document.save()
        data = data[1:]
        for document_group in split(data, 25):
            first_class.objects.insert(document_group)
        return


if __name__ == "__main__":
    parker = Parker()
    logger.debug("Starting")
    park_data = parker.get_all_park_data()
    print(park_data)
