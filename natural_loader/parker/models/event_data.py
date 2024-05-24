import pprint

import six
from mongoengine import DictField, ListField, StringField

from natural_loader.parker.models.base_document import BaseDocument


class EventData(BaseDocument):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    contactemailaddress = StringField()
    contactname = StringField()
    contacttelephone_number = StringField()
    category = StringField()
    categoryid = StringField()
    createuser = StringField()
    dateend = StringField()
    _date = StringField()
    dates = ListField(StringField())
    datestart = StringField()
    datetimecreated = StringField()
    datetimeupdated = StringField()
    description = StringField()
    eventid = StringField()
    feeinfo = StringField()
    geometry_poi_id = StringField()
    id = StringField()
    imageidlist = StringField()
    images = ListField(DictField())
    infourl = StringField()
    isallday = StringField()
    isfree = StringField()
    isrecurring = StringField()
    isregresrequired = StringField()
    latitude = StringField()
    location = StringField()
    longitude = StringField()
    organizationname = StringField()
    parkfullname = StringField()
    portalname = StringField()
    recurrencedateend = StringField()
    recurrencedatestart = StringField()
    recurrencerule = StringField()
    regresinfo = StringField()
    regresurl = StringField()
    sitecode = StringField()
    sitetype = StringField()
    subjectname = StringField()
    tags = ListField(StringField())
    timeinfo = StringField()
    times = ListField(DictField())
    title = StringField()
    types = ListField(StringField())
    meta = {"collection": "event_data"}

    swagger_types = {
        "contactemailaddress": "str",
        "contactname": "str",
        "contacttelephone_number": "str",
        "category": "str",
        "categoryid": "str",
        "createuser": "str",
        "dateend": "datetime",
        "_date": "datetime",
        "dates": "list[datetime]",
        "datestart": "datetime",
        "datetimecreated": "str",
        "datetimeupdated": "str",
        "description": "str",
        "eventid": "str",
        "feeinfo": "str",
        "geometry_poi_id": "str",
        "id": "str",
        "imageidlist": "str",
        "images": "list[EventImages]",
        "infourl": "str",
        "isallday": "str",
        "isfree": "str",
        "isrecurring": "str",
        "isregresrequired": "str",
        "latitude": "str",
        "location": "str",
        "longitude": "str",
        "organizationname": "str",
        "parkfullname": "str",
        "portalname": "str",
        "recurrencedateend": "datetime",
        "recurrencedatestart": "datetime",
        "recurrencerule": "str",
        "regresinfo": "str",
        "regresurl": "str",
        "sitecode": "str",
        "sitetype": "str",
        "subjectname": "str",
        "tags": "list[str]",
        "timeinfo": "str",
        "times": "list[EventTimes]",
        "title": "str",
        "types": "list[str]",
    }

    attribute_map = {
        "contactemailaddress": "contactemailaddress",
        "contactname": "contactname",
        "contacttelephone_number": "contacttelephoneNumber",
        "category": "category",
        "categoryid": "categoryid",
        "createuser": "createuser",
        "dateend": "dateend",
        "_date": "date",
        "dates": "dates",
        "datestart": "datestart",
        "datetimecreated": "datetimecreated",
        "datetimeupdated": "datetimeupdated",
        "description": "description",
        "eventid": "eventid",
        "feeinfo": "feeinfo",
        "geometry_poi_id": "geometryPoiId",
        "id": "id",
        "imageidlist": "imageidlist",
        "images": "images",
        "infourl": "infourl",
        "isallday": "isallday",
        "isfree": "isfree",
        "isrecurring": "isrecurring",
        "isregresrequired": "isregresrequired",
        "latitude": "latitude",
        "location": "location",
        "longitude": "longitude",
        "organizationname": "organizationname",
        "parkfullname": "parkfullname",
        "portalname": "portalname",
        "recurrencedateend": "recurrencedateend",
        "recurrencedatestart": "recurrencedatestart",
        "recurrencerule": "recurrencerule",
        "regresinfo": "regresinfo",
        "regresurl": "regresurl",
        "sitecode": "sitecode",
        "sitetype": "sitetype",
        "subjectname": "subjectname",
        "tags": "tags",
        "timeinfo": "timeinfo",
        "times": "times",
        "title": "title",
        "types": "types",
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
        if issubclass(EventData, dict):
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
        if not isinstance(other, EventData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventData):
            return True

        return self.to_dict() != other.to_dict()
