# coding: utf-8

# flake8: noqa

"""
    Divseek Canada MVP application API

    Implements all the calls necessary for finding genomic markers for germplasm, but doesn't conform to BrAPI.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.default_api import DefaultApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.api_response import ApiResponse
from swagger_client.models.germplasm import Germplasm
from swagger_client.models.locus import Locus
from swagger_client.models.phenotype import Phenotype
from swagger_client.models.qtl import QTL
from swagger_client.models.query import Query
from swagger_client.models.taxonomy import Taxonomy
