# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class ExternalAccountUserAttributionChannel(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, external_account_id=None, active=None, url=None):
        """
        ExternalAccountUserAttributionChannel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'external_account_id': 'int',
            'active': 'bool',
            'url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'external_account_id': 'external_account_id',
            'active': 'active',
            'url': 'url'
        }

        self._id = id
        self._external_account_id = external_account_id
        self._active = active
        self._url = url

    @property
    def id(self):
        """
        Gets the id of this ExternalAccountUserAttributionChannel.
        Unique ID

        :return: The id of this ExternalAccountUserAttributionChannel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalAccountUserAttributionChannel.
        Unique ID

        :param id: The id of this ExternalAccountUserAttributionChannel.
        :type: int
        """

        self._id = id

    @property
    def external_account_id(self):
        """
        Gets the external_account_id of this ExternalAccountUserAttributionChannel.
        The ID of the external account this channel is for

        :return: The external_account_id of this ExternalAccountUserAttributionChannel.
        :rtype: int
        """
        return self._external_account_id

    @external_account_id.setter
    def external_account_id(self, external_account_id):
        """
        Sets the external_account_id of this ExternalAccountUserAttributionChannel.
        The ID of the external account this channel is for

        :param external_account_id: The external_account_id of this ExternalAccountUserAttributionChannel.
        :type: int
        """

        self._external_account_id = external_account_id

    @property
    def active(self):
        """
        Gets the active of this ExternalAccountUserAttributionChannel.
        If the channel is active

        :return: The active of this ExternalAccountUserAttributionChannel.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ExternalAccountUserAttributionChannel.
        If the channel is active

        :param active: The active of this ExternalAccountUserAttributionChannel.
        :type: bool
        """

        self._active = active

    @property
    def url(self):
        """
        Gets the url of this ExternalAccountUserAttributionChannel.
        The URL for the channel

        :return: The url of this ExternalAccountUserAttributionChannel.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ExternalAccountUserAttributionChannel.
        The URL for the channel

        :param url: The url of this ExternalAccountUserAttributionChannel.
        :type: str
        """

        self._url = url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ExternalAccountUserAttributionChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other