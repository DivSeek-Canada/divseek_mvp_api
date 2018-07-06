# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.germplasm import Germplasm  # noqa: E501
from swagger_server.models.locus import Locus  # noqa: E501
from swagger_server.models.phenotype import Phenotype  # noqa: E501
from swagger_server.models.qtl import QTL  # noqa: E501
from swagger_server.models.taxonomy import Taxonomy  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_germplasm(self):
        """Test case for get_germplasm

        Returns all germplasm we have
        """
        response = self.client.open(
            '/v2/germplasm/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_germplasm_by_id(self):
        """Test case for get_germplasm_by_id

        Returns all germplasm we have
        """
        response = self.client.open(
            '/v2/germplasm/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_germplasm_by_taxon(self):
        """Test case for get_germplasm_by_taxon

        Returns all germplasm we have by taxon
        """
        response = self.client.open(
            '/v2/germplasm/taxon/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_locus_by_qtl(self):
        """Test case for get_locus_by_qtl

        Returns all phenotypes for a germplasm that we have
        """
        response = self.client.open(
            '/v2/locus/qtl/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_locus_by_taxon(self):
        """Test case for get_locus_by_taxon

        Returns all phenotypes for a germplasm that we have
        """
        response = self.client.open(
            '/v2/locus/taxon/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_qt_ls(self):
        """Test case for get_qt_ls

        Returns all the QTLs (Quantitative Trait Loci) we have
        """
        response = self.client.open(
            '/v2/qtl/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_qtl_by_germplasm_trait(self):
        """Test case for get_qtl_by_germplasm_trait

        Returns all phenotypes for a germplasm that we have
        """
        response = self.client.open(
            '/v2/qtl/taxon/{taxonId}/trait/{traitId}'.format(germplasmId='germplasmId_example', traitId='traitId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_taxonomy(self):
        """Test case for get_taxonomy

        Returns all germplasm we have
        """
        response = self.client.open(
            '/v2/taxon/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_taxonomy_by_id(self):
        """Test case for get_taxonomy_by_id

        Returns all germplasm we have
        """
        response = self.client.open(
            '/v2/taxon/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_traits(self):
        """Test case for get_traits

        Returns all phenotypes we have
        """
        response = self.client.open(
            '/v2/trait/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_traits_by_germplasm(self):
        """Test case for get_traits_by_germplasm

        Returns all phenotypes for a germplasm that we have
        """
        response = self.client.open(
            '/v2/trait/germplasm/{germplasmId}'.format(germplasmId='germplasmId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
