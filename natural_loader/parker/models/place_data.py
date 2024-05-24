import pprint

import six
from mongoengine import DictField, ListField, StringField

from natural_loader.parker.models.base_document import BaseDocument


class PlaceData(BaseDocument):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    lat_long = StringField()
    longitude = StringField()
    geometry_poi_id = StringField()
    id = StringField()
    latitude = StringField()
    listing_description = StringField()
    related_parks = DictField()
    title = StringField()
    url = StringField()
    images = ListField(StringField())
    amenities = ListField(StringField())
    quick_facts = StringField()
    npmap_id = StringField()
    tags = ListField(StringField())
    related_organizations = ListField(StringField())
    audio_description = StringField()
    managed_by_url = StringField()
    is_open_to_public = StringField()
    is_managed_by_nps = StringField()
    managed_by_org = StringField()
    body_text = StringField()
    multimedia = ListField(DictField())

    swagger_types = {
        "lat_long": "str",
        "longitude": "str",
        "geometry_poi_id": "str",
        "id": "str",
        "latitude": "str",
        "listing_description": "str",
        "related_parks": "list[PlaceRelatedParks]",
        "title": "str",
        "url": "str",
        "images": "list[str]",
        "amenities": "list[str]",
        "quick_facts": "str",
        "npmap_id": "str",
        "tags": "list[str]",
        "related_organizations": "list[str]",
        "audio_description": "str",
        "managed_by_url": "str",
        "is_open_to_public": "str",
        "is_managed_by_nps": "str",
        "managed_by_org": "str",
        "body_text": "str",
        "multimedia": "list[PlaceMultimedia]",
    }

    attribute_map = {
        "lat_long": "latLong",
        "longitude": "longitude",
        "geometry_poi_id": "geometryPoiId",
        "id": "id",
        "latitude": "latitude",
        "listing_description": "listingDescription",
        "related_parks": "relatedParks",
        "title": "title",
        "url": "url",
        "images": "images",
        "amenities": "amenities",
        "quick_facts": "quickFacts",
        "npmap_id": "npmapId",
        "tags": "tags",
        "related_organizations": "relatedOrganizations",
        "audio_description": "audioDescription",
        "managed_by_url": "managedByUrl",
        "is_open_to_public": "isOpenToPublic",
        "is_managed_by_nps": "isManagedByNps",
        "managed_by_org": "managedByOrg",
        "body_text": "bodyText",
        "multimedia": "multimedia",
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
        if issubclass(PlaceData, dict):
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
        if not isinstance(other, PlaceData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlaceData):
            return True

        return self.to_dict() != other.to_dict()
