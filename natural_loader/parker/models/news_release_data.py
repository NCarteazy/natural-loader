import pprint

import six
from mongoengine import DateTimeField, StringField

from natural_loader.parker.models.base_document import BaseDocument


class NewsReleaseData(BaseDocument):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    abstract = StringField()
    geometry_poi_id = StringField()
    id = StringField()
    latitude = StringField()
    longitude = StringField()
    park_code = StringField()
    releasedate = DateTimeField()
    title = StringField()
    url = StringField()

    swagger_types = {
        "abstract": "str",
        "geometry_poi_id": "str",
        "id": "str",
        "latitude": "str",
        "longitude": "str",
        "park_code": "str",
        "releasedate": "datetime",
        "title": "str",
        "url": "str",
    }

    attribute_map = {
        "abstract": "abstract",
        "geometry_poi_id": "geometryPoiId",
        "id": "id",
        "image": "image",
        "latitude": "latitude",
        "longitude": "longitude",
        "park_code": "parkCode",
        "related_orgs": "relatedOrgs",
        "related_parks": "relatedParks",
        "releasedate": "releasedate",
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
        if issubclass(NewsReleaseData, dict):
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
        if not isinstance(other, NewsReleaseData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewsReleaseData):
            return True

        return self.to_dict() != other.to_dict()
