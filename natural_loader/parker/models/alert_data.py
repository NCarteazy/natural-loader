import pprint

import six
from mongoengine import DictField, ListField, StringField

from natural_loader.parker.models.base_document import BaseDocument


class AlertData(BaseDocument):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    category = StringField()
    description = StringField()
    id = StringField()
    park_code = StringField()
    title = StringField()
    url = StringField()
    last_indexed_date = StringField()
    related_road_events = ListField(DictField())
    meta = {"collection": "alert_data"}

    swagger_types = {
        "category": "str",
        "description": "str",
        "id": "str",
        "park_code": "str",
        "title": "str",
        "url": "str",
        "last_indexed_date": "str",
        "related_road_events": "list[AlertRelatedRoadEvents]",
    }

    attribute_map = {
        "category": "category",
        "description": "description",
        "id": "id",
        "park_code": "parkCode",
        "title": "title",
        "url": "url",
        "last_indexed_date": "lastIndexedDate",
        "related_road_events": "relatedRoadEvents",
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
        if issubclass(AlertData, dict):
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
        if not isinstance(other, AlertData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertData):
            return True

        return self.to_dict() != other.to_dict()
