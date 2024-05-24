import pprint

import six
from mongoengine import DictField, FloatField, ListField, StringField

from natural_loader.parker.models.base_document import BaseDocument


class CampgroundData(BaseDocument):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    accessibility = DictField()
    addresses = ListField(DictField())
    amenities = DictField()
    campsites = DictField()
    contacts = DictField()
    description = StringField()
    directionsoverview = StringField()
    directions_url = StringField()
    fees = ListField(StringField())
    geometry_poi_id = StringField()
    id = StringField(required=True, primary_key=True)
    images = ListField(StringField())
    last_indexed_date = StringField()
    lat_long = StringField()
    latitude = StringField()
    longitude = StringField()
    multimedia = ListField(DictField())
    name = StringField()
    operating_hours = ListField(StringField())
    park_code = StringField()
    regulationsoverview = StringField()
    regulationsurl = StringField()
    relevance_score = FloatField()
    reservationsdescription = StringField()
    reservationssitesfirstcome = StringField()
    reservationssitesreservable = StringField()
    reservationsurl = StringField()
    weatheroverview = StringField()
    meta = {"collection": "campground_data"}

    swagger_types = {
        "addresses": "list[CampgroundAddresses]",
        "amenities": "CampgroundAmenities",
        "campsites": "CampgroundCampsites",
        "contacts": "CampgroundContacts",
        "description": "str",
        "directionsoverview": "str",
        "directions_url": "str",
        "fees": "list[str]",
        "geometry_poi_id": "str",
        "id": "str",
        "images": "list[str]",
        "last_indexed_date": "str",
        "lat_long": "str",
        "latitude": "str",
        "longitude": "str",
        "multimedia": "list[CampgroundMultimedia]",
        "name": "str",
        "operating_hours": "list[str]",
        "park_code": "str",
        "regulationsoverview": "str",
        "regulationsurl": "str",
        "relevance_score": "float",
        "reservationsdescription": "str",
        "reservationssitesfirstcome": "str",
        "reservationssitesreservable": "str",
        "reservationsurl": "str",
        "weatheroverview": "str",
    }

    attribute_map = {
        "accessibility": "accessibility",
        "addresses": "addresses",
        "amenities": "amenities",
        "campsites": "campsites",
        "contacts": "contacts",
        "description": "description",
        "directionsoverview": "directionsoverview",
        "directions_url": "directionsUrl",
        "fees": "fees",
        "geometry_poi_id": "geometryPoiId",
        "id": "id",
        "images": "images",
        "last_indexed_date": "lastIndexedDate",
        "lat_long": "latLong",
        "latitude": "latitude",
        "longitude": "longitude",
        "multimedia": "multimedia",
        "name": "name",
        "operating_hours": "operatingHours",
        "park_code": "parkCode",
        "regulationsoverview": "regulationsoverview",
        "regulationsurl": "regulationsurl",
        "relevance_score": "relevanceScore",
        "reservationsdescription": "reservationsdescription",
        "reservationssitesfirstcome": "reservationssitesfirstcome",
        "reservationssitesreservable": "reservationssitesreservable",
        "reservationsurl": "reservationsurl",
        "weatheroverview": "weatheroverview",
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
        if issubclass(CampgroundData, dict):
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
        if not isinstance(other, CampgroundData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampgroundData):
            return True

        return self.to_dict() != other.to_dict()
