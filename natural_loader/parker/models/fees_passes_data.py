import pprint

import six
from mongoengine import DictField, ListField, StringField

from natural_loader.parker.models.base_document import BaseDocument


class FeesPassesData(BaseDocument):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    cashless = StringField()
    entrance_fee_description = StringField()
    entrance_passes_description = StringField()
    fees = ListField(DictField())
    fees_at_work_url = StringField()
    is_fee_free_park = StringField()
    is_interagency_pass_accepted = StringField()
    is_parking_fee_possible = StringField()
    park_code = StringField()
    parking_details_url = StringField()
    passes = ListField(DictField())
    timed_entry_heading = StringField()
    timed_entry_description = StringField()
    is_parking_or_transportation_fee_possible = StringField()
    paid_parking_heading = StringField()
    paid_parking_description = StringField()
    custom_fee_heading = StringField()
    custom_fee_description = StringField()
    custom_fee_link_url = StringField()
    custom_fee_link_text = StringField()
    content_order_ordinals = StringField()
    related_multi_site_passes = ListField(DictField())
    meta = {"collection": "fees_passes_data"}

    swagger_types = {
        "cashless": "str",
        "entrance_fee_description": "str",
        "entrance_passes_description": "str",
        "fees": "list[FeesPassesFees]",
        "fees_at_work_url": "str",
        "is_fee_free_park": "bool",
        "is_interagency_pass_accepted": "bool",
        "is_parking_fee_possible": "bool",
        "park_code": "str",
        "parking_details_url": "str",
        "passes": "list[FeesPassesPasses]",
        "timed_entry_heading": "str",
        "timed_entry_description": "str",
        "is_parking_or_transportation_fee_possible": "bool",
        "paid_parking_heading": "str",
        "paid_parking_description": "str",
        "custom_fee_heading": "str",
        "custom_fee_description": "str",
        "custom_fee_link_url": "str",
        "custom_fee_link_text": "str",
        "content_order_ordinals": "str",
        "related_multi_site_passes": "list[FeesPassesRelatedMultiSitePasses]",
    }

    attribute_map = {
        "cashless": "cashless",
        "entrance_fee_description": "entranceFeeDescription",
        "entrance_passes_description": "entrancePassesDescription",
        "fees": "fees",
        "fees_at_work_url": "feesAtWorkUrl",
        "is_fee_free_park": "isFeeFreePark",
        "is_interagency_pass_accepted": "isInteragencyPassAccepted",
        "is_parking_fee_possible": "isParkingFeePossible",
        "park_code": "parkCode",
        "parking_details_url": "parkingDetailsUrl",
        "passes": "passes",
        "timed_entry_heading": "timedEntryHeading",
        "timed_entry_description": "timedEntryDescription",
        "is_parking_or_transportation_fee_possible": "isParkingOrTransportationFeePossible",
        "paid_parking_heading": "paidParkingHeading",
        "paid_parking_description": "paidParkingDescription",
        "custom_fee_heading": "customFeeHeading",
        "custom_fee_description": "customFeeDescription",
        "custom_fee_link_url": "customFeeLinkUrl",
        "custom_fee_link_text": "customFeeLinkText",
        "content_order_ordinals": "contentOrderOrdinals",
        "related_multi_site_passes": "relatedMultiSitePasses",
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
        if issubclass(FeesPassesData, dict):
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
        if not isinstance(other, FeesPassesData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeesPassesData):
            return True

        return self.to_dict() != other.to_dict()
