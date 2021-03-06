# coding: utf-8

"""
    Divseek Canada MVP application API

    Implements all the calls necessary for finding genomic markers for germplasm, but doesn't conform to BrAPI.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_germplasm(self):
        """Test case for get_germplasm

        Returns all germplasm we have  # noqa: E501
        """
        pass

    def test_get_germplasm_by_id(self):
        """Test case for get_germplasm_by_id

        Returns all germplasm we have  # noqa: E501
        """
        pass

    def test_get_germplasm_by_taxon(self):
        """Test case for get_germplasm_by_taxon

        Returns all germplasm we have by taxon  # noqa: E501
        """
        pass

    def test_get_locus_by_qtl(self):
        """Test case for get_locus_by_qtl

        Returns all phenotypes for a germplasm that we have  # noqa: E501
        """
        pass

    def test_get_locus_by_taxon(self):
        """Test case for get_locus_by_taxon

        Returns all phenotypes for a germplasm that we have  # noqa: E501
        """
        pass

    def test_get_qt_ls(self):
        """Test case for get_qt_ls

        Returns all the QTLs (Quantitative Trait Loci) we have  # noqa: E501
        """
        pass

    def test_get_qtl_by_germplasm_trait(self):
        """Test case for get_qtl_by_germplasm_trait

        Returns all phenotypes for a germplasm that we have  # noqa: E501
        """
        pass

    def test_get_taxonomy(self):
        """Test case for get_taxonomy

        Returns all germplasm we have  # noqa: E501
        """
        pass

    def test_get_taxonomy_by_id(self):
        """Test case for get_taxonomy_by_id

        Returns all germplasm we have  # noqa: E501
        """
        pass

    def test_get_traits(self):
        """Test case for get_traits

        Returns all phenotypes we have  # noqa: E501
        """
        pass

    def test_get_traits_by_germplasm(self):
        """Test case for get_traits_by_germplasm

        Returns all phenotypes for a germplasm that we have  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
