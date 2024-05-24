from typing import Type, TypeVar

from mongoengine import Document

T = TypeVar("T", bound="BaseDocument")


class BaseDocument(Document):
    attribute_map = {}
    meta = {"abstract": True}

    @classmethod
    def from_dict(cls: Type[T], dikt: dict) -> T:
        return cls(**dikt)

    @classmethod
    def from_list_dicts(cls: Type[T], list_of_dicts: list[dict]) -> list[T]:
        return [cls.from_response(dikt) for dikt in list_of_dicts]

    @classmethod
    def from_response(cls: Type[T], response: dict) -> T:
        return cls.from_dict(cls.response_to_attribute_map(response))

    @classmethod
    def response_to_attribute_map(cls: Type[T], response: dict) -> dict:
        """
        Takes a response from the API and returns a dictionary with the keys as the attribute names
        and the values as the values from the response.
        """
        return {k: response[v] for k, v in cls.attribute_map.items()}
