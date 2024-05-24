import pprint

import six
from mongoengine import DictField, FloatField, ListField, StringField

from natural_loader.parker.models.base_document import BaseDocument


class ParkData(BaseDocument):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    # meta = {"indexes": ["full_name", "name", "states"], "collection": "park_data"}

    activities = ListField(DictField())
    addresses = ListField(DictField())
    contacts = DictField()
    description = StringField()
    designation = StringField()
    directions_info = StringField()
    directions_url = StringField()
    entrance_fees = ListField(DictField())
    entrance_passes = ListField(DictField())
    full_name = StringField(unique=True)
    images = ListField(DictField())
    lat_long = StringField()
    latitude = StringField()
    longitude = StringField()
    multimedia = ListField(DictField())
    name = StringField(unique=True)
    operating_hours = ListField(DictField())
    park_code = StringField()
    relevance_score = FloatField()
    states = StringField()
    topics = ListField(DictField())
    url = StringField()
    weather_info = StringField()

    swagger_types = {
        "activities": "list[ParkActivities]",
        "addresses": "list[ParkAddresses]",
        "contacts": "ParkContacts",
        "description": "str",
        "designation": "str",
        "directions_info": "str",
        "directions_url": "str",
        "entrance_fees": "list[ParkEntranceFees]",
        "entrance_passes": "list[ParkEntranceFees]",
        "full_name": "str",
        "images": "list[ParkImages]",
        "lat_long": "str",
        "latitude": "str",
        "longitude": "str",
        "multimedia": "list[CampgroundMultimedia]",
        "name": "str",
        "operating_hours": "list[ParkOperatingHours]",
        "park_code": "str",
        "relevance_score": "float",
        "states": "str",
        "topics": "list[ParkActivities]",
        "url": "str",
        "weather_info": "str",
    }

    attribute_map = {
        "activities": "activities",
        "addresses": "addresses",
        "contacts": "contacts",
        "description": "description",
        "designation": "designation",
        "directions_info": "directionsInfo",
        "directions_url": "directionsUrl",
        "entrance_fees": "entranceFees",
        "entrance_passes": "entrancePasses",
        "full_name": "fullName",
        "images": "images",
        "lat_long": "latLong",
        "latitude": "latitude",
        "longitude": "longitude",
        "multimedia": "multimedia",
        "name": "name",
        "operating_hours": "operatingHours",
        "park_code": "parkCode",
        "relevance_score": "relevanceScore",
        "states": "states",
        "topics": "topics",
        "url": "url",
        "weather_info": "weatherInfo",
    }

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ParkData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ParkData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParkData):
            return True

        return self.to_dict() != other.to_dict()
