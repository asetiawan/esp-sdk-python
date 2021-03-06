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


class ComplianceDomain(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, identifier=None, name=None, created_at=None, updated_at=None, position=None, compliance_standard=None, compliance_standard_id=None, compliance_controls=None, compliance_control_ids=None):
        """
        ComplianceDomain - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'identifier': 'str',
            'name': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'position': 'int',
            'compliance_standard': 'ComplianceStandard',
            'compliance_standard_id': 'int',
            'compliance_controls': 'list[ComplianceControl]',
            'compliance_control_ids': 'list[int]'
        }

        self.attribute_map = {
            'id': 'id',
            'identifier': 'identifier',
            'name': 'name',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'position': 'position',
            'compliance_standard': 'compliance_standard',
            'compliance_standard_id': 'compliance_standard_id',
            'compliance_controls': 'compliance_controls',
            'compliance_control_ids': 'compliance_control_ids'
        }

        self._id = id
        self._identifier = identifier
        self._name = name
        self._created_at = created_at
        self._updated_at = updated_at
        self._position = position
        self._compliance_standard = compliance_standard
        self._compliance_standard_id = compliance_standard_id
        self._compliance_controls = compliance_controls
        self._compliance_control_ids = compliance_control_ids

    @property
    def id(self):
        """
        Gets the id of this ComplianceDomain.
        Unique ID

        :return: The id of this ComplianceDomain.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComplianceDomain.
        Unique ID

        :param id: The id of this ComplianceDomain.
        :type: int
        """

        self._id = id

    @property
    def identifier(self):
        """
        Gets the identifier of this ComplianceDomain.
        The identifier of this domain

        :return: The identifier of this ComplianceDomain.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ComplianceDomain.
        The identifier of this domain

        :param identifier: The identifier of this ComplianceDomain.
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """
        Gets the name of this ComplianceDomain.
        Name

        :return: The name of this ComplianceDomain.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ComplianceDomain.
        Name

        :param name: The name of this ComplianceDomain.
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """
        Gets the created_at of this ComplianceDomain.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this ComplianceDomain.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ComplianceDomain.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this ComplianceDomain.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ComplianceDomain.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this ComplianceDomain.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ComplianceDomain.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this ComplianceDomain.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def position(self):
        """
        Gets the position of this ComplianceDomain.
        The position of this domain within the Standard

        :return: The position of this ComplianceDomain.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ComplianceDomain.
        The position of this domain within the Standard

        :param position: The position of this ComplianceDomain.
        :type: int
        """

        self._position = position

    @property
    def compliance_standard(self):
        """
        Gets the compliance_standard of this ComplianceDomain.
        Associated Compliance Standard

        :return: The compliance_standard of this ComplianceDomain.
        :rtype: ComplianceStandard
        """
        return self._compliance_standard

    @compliance_standard.setter
    def compliance_standard(self, compliance_standard):
        """
        Sets the compliance_standard of this ComplianceDomain.
        Associated Compliance Standard

        :param compliance_standard: The compliance_standard of this ComplianceDomain.
        :type: ComplianceStandard
        """

        self._compliance_standard = compliance_standard

    @property
    def compliance_standard_id(self):
        """
        Gets the compliance_standard_id of this ComplianceDomain.
        Associated Compliance Standard ID

        :return: The compliance_standard_id of this ComplianceDomain.
        :rtype: int
        """
        return self._compliance_standard_id

    @compliance_standard_id.setter
    def compliance_standard_id(self, compliance_standard_id):
        """
        Sets the compliance_standard_id of this ComplianceDomain.
        Associated Compliance Standard ID

        :param compliance_standard_id: The compliance_standard_id of this ComplianceDomain.
        :type: int
        """

        self._compliance_standard_id = compliance_standard_id

    @property
    def compliance_controls(self):
        """
        Gets the compliance_controls of this ComplianceDomain.
        Associated Compliance Controls

        :return: The compliance_controls of this ComplianceDomain.
        :rtype: list[ComplianceControl]
        """
        return self._compliance_controls

    @compliance_controls.setter
    def compliance_controls(self, compliance_controls):
        """
        Sets the compliance_controls of this ComplianceDomain.
        Associated Compliance Controls

        :param compliance_controls: The compliance_controls of this ComplianceDomain.
        :type: list[ComplianceControl]
        """

        self._compliance_controls = compliance_controls

    @property
    def compliance_control_ids(self):
        """
        Gets the compliance_control_ids of this ComplianceDomain.
        Associated Compliance Controls IDs

        :return: The compliance_control_ids of this ComplianceDomain.
        :rtype: list[int]
        """
        return self._compliance_control_ids

    @compliance_control_ids.setter
    def compliance_control_ids(self, compliance_control_ids):
        """
        Sets the compliance_control_ids of this ComplianceDomain.
        Associated Compliance Controls IDs

        :param compliance_control_ids: The compliance_control_ids of this ComplianceDomain.
        :type: list[int]
        """

        self._compliance_control_ids = compliance_control_ids

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
        if not isinstance(other, ComplianceDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
