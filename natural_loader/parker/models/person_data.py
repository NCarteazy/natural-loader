import pprint

import six
from mongoengine import DictField, StringField

from natural_loader.parker.models.base_document import BaseDocument


class PersonData(BaseDocument):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    body_text = StringField()
    id = StringField()
    geometry_poi_id = StringField()
    first_name = StringField()
    middle_name = StringField()
    last_name = StringField()
    images = DictField()
    lat_long = StringField()
    latitude = StringField()
    listing_description = StringField()
    longitude = StringField()
    quick_facts = DictField()
    related_organizations = DictField()
    related_parks = DictField()
    title = StringField()
    url = StringField()

    swagger_types = {
        "body_text": "str",
        "id": "str",
        "geometry_poi_id": "str",
        "first_name": "str",
        "middle_name": "str",
        "last_name": "str",
        "images": "list[PersonImages]",
        "lat_long": "str",
        "latitude": "str",
        "listing_description": "str",
        "longitude": "str",
        "quick_facts": "list[PersonQuickFacts]",
        "related_organizations": "list[object]",
        "related_parks": "list[PersonRelatedParks]",
        "title": "str",
        "url": "str",
    }

    attribute_map = {
        "body_text": "bodyText",
        "id": "id",
        "geometry_poi_id": "geometryPoiId",
        "first_name": "firstName",
        "middle_name": "middleName",
        "last_name": "lastName",
        "images": "images",
        "lat_long": "latLong",
        "latitude": "latitude",
        "listing_description": "listingDescription",
        "longitude": "longitude",
        "quick_facts": "quickFacts",
        "related_organizations": "relatedOrganizations",
        "related_parks": "relatedParks",
        "title": "title",
        "url": "url",
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
        if issubclass(PersonData, dict):
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
        if not isinstance(other, PersonData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PersonData):
            return True

        return self.to_dict() != other.to_dict()
