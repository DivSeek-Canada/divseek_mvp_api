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


class Taxonomy(object):
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
        'taxonomy_id': 'int',
        'genus': 'str',
        'species': 'str'
    }

    attribute_map = {
        'taxonomy_id': 'taxonomy_id',
        'genus': 'genus',
        'species': 'species'
    }

    def __init__(self, taxonomy_id=None, genus=None, species=None):  # noqa: E501
        """Taxonomy - a model defined in Swagger"""  # noqa: E501

        self._taxonomy_id = None
        self._genus = None
        self._species = None
        self.discriminator = None

        self.taxonomy_id = taxonomy_id
        if genus is not None:
            self.genus = genus
        if species is not None:
            self.species = species

    @property
    def taxonomy_id(self):
        """Gets the taxonomy_id of this Taxonomy.  # noqa: E501


        :return: The taxonomy_id of this Taxonomy.  # noqa: E501
        :rtype: int
        """
        return self._taxonomy_id

    @taxonomy_id.setter
    def taxonomy_id(self, taxonomy_id):
        """Sets the taxonomy_id of this Taxonomy.


        :param taxonomy_id: The taxonomy_id of this Taxonomy.  # noqa: E501
        :type: int
        """
        if taxonomy_id is None:
            raise ValueError("Invalid value for `taxonomy_id`, must not be `None`")  # noqa: E501

        self._taxonomy_id = taxonomy_id

    @property
    def genus(self):
        """Gets the genus of this Taxonomy.  # noqa: E501


        :return: The genus of this Taxonomy.  # noqa: E501
        :rtype: str
        """
        return self._genus

    @genus.setter
    def genus(self, genus):
        """Sets the genus of this Taxonomy.


        :param genus: The genus of this Taxonomy.  # noqa: E501
        :type: str
        """

        self._genus = genus

    @property
    def species(self):
        """Gets the species of this Taxonomy.  # noqa: E501


        :return: The species of this Taxonomy.  # noqa: E501
        :rtype: str
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this Taxonomy.


        :param species: The species of this Taxonomy.  # noqa: E501
        :type: str
        """

        self._species = species

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
        if not isinstance(other, Taxonomy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other