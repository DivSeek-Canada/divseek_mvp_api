# coding: utf-8

"""
    Divseek Canada MVP application API

    Implements all the calls necessary for finding genomic markers for germplasm, but doesn't conform to BrAPI.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Locus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'locus_id': 'int',
        'locus_name': 'str',
        'basepair_start': 'int',
        'basepair_end': 'int',
        'taxonomy_id': 'int'
    }

    attribute_map = {
        'locus_id': 'locus_id',
        'locus_name': 'locus_name',
        'basepair_start': 'basepair_start',
        'basepair_end': 'basepair_end',
        'taxonomy_id': 'taxonomy_id'
    }

    def __init__(self, locus_id=None, locus_name=None, basepair_start=None, basepair_end=None, taxonomy_id=None):  # noqa: E501
        """Locus - a model defined in Swagger"""  # noqa: E501

        self._locus_id = None
        self._locus_name = None
        self._basepair_start = None
        self._basepair_end = None
        self._taxonomy_id = None
        self.discriminator = None

        self.locus_id = locus_id
        if locus_name is not None:
            self.locus_name = locus_name
        self.basepair_start = basepair_start
        self.basepair_end = basepair_end
        if taxonomy_id is not None:
            self.taxonomy_id = taxonomy_id

    @property
    def locus_id(self):
        """Gets the locus_id of this Locus.  # noqa: E501


        :return: The locus_id of this Locus.  # noqa: E501
        :rtype: int
        """
        return self._locus_id

    @locus_id.setter
    def locus_id(self, locus_id):
        """Sets the locus_id of this Locus.


        :param locus_id: The locus_id of this Locus.  # noqa: E501
        :type: int
        """
        if locus_id is None:
            raise ValueError("Invalid value for `locus_id`, must not be `None`")  # noqa: E501

        self._locus_id = locus_id

    @property
    def locus_name(self):
        """Gets the locus_name of this Locus.  # noqa: E501


        :return: The locus_name of this Locus.  # noqa: E501
        :rtype: str
        """
        return self._locus_name

    @locus_name.setter
    def locus_name(self, locus_name):
        """Sets the locus_name of this Locus.


        :param locus_name: The locus_name of this Locus.  # noqa: E501
        :type: str
        """

        self._locus_name = locus_name

    @property
    def basepair_start(self):
        """Gets the basepair_start of this Locus.  # noqa: E501


        :return: The basepair_start of this Locus.  # noqa: E501
        :rtype: int
        """
        return self._basepair_start

    @basepair_start.setter
    def basepair_start(self, basepair_start):
        """Sets the basepair_start of this Locus.


        :param basepair_start: The basepair_start of this Locus.  # noqa: E501
        :type: int
        """
        if basepair_start is None:
            raise ValueError("Invalid value for `basepair_start`, must not be `None`")  # noqa: E501

        self._basepair_start = basepair_start

    @property
    def basepair_end(self):
        """Gets the basepair_end of this Locus.  # noqa: E501


        :return: The basepair_end of this Locus.  # noqa: E501
        :rtype: int
        """
        return self._basepair_end

    @basepair_end.setter
    def basepair_end(self, basepair_end):
        """Sets the basepair_end of this Locus.


        :param basepair_end: The basepair_end of this Locus.  # noqa: E501
        :type: int
        """
        if basepair_end is None:
            raise ValueError("Invalid value for `basepair_end`, must not be `None`")  # noqa: E501

        self._basepair_end = basepair_end

    @property
    def taxonomy_id(self):
        """Gets the taxonomy_id of this Locus.  # noqa: E501


        :return: The taxonomy_id of this Locus.  # noqa: E501
        :rtype: int
        """
        return self._taxonomy_id

    @taxonomy_id.setter
    def taxonomy_id(self, taxonomy_id):
        """Sets the taxonomy_id of this Locus.


        :param taxonomy_id: The taxonomy_id of this Locus.  # noqa: E501
        :type: int
        """

        self._taxonomy_id = taxonomy_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Locus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other