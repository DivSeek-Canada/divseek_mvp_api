import connexion
import six

from swagger_server.models.germplasm import Germplasm  # noqa: E501
from swagger_server.models.locus import Locus  # noqa: E501
from swagger_server.models.phenotype import Phenotype  # noqa: E501
from swagger_server.models.qtl import QTL  # noqa: E501
from swagger_server.models.taxonomy import Taxonomy  # noqa: E501
from swagger_server import util


def get_germplasm():  # noqa: E501
    """Returns all germplasm we have

     # noqa: E501


    :rtype: List[Germplasm]
    """
    return 'do some magic!'


def get_germplasm_by_id(id):  # noqa: E501
    """Returns all germplasm we have

     # noqa: E501

    :param id: Unique database ID for the germplasm
    :type id: str

    :rtype: Germplasm
    """
    return 'do some magic!'


def get_germplasm_by_taxon(id):  # noqa: E501
    """Returns all germplasm we have by taxon

     # noqa: E501

    :param id: Unique database ID for the taxon
    :type id: str

    :rtype: Germplasm
    """
    return 'do some magic!'


def get_locus_by_qtl(id):  # noqa: E501
    """Returns all phenotypes for a germplasm that we have

     # noqa: E501

    :param id: Unique database ID for the QTL
    :type id: str

    :rtype: Locus
    """
    return 'do some magic!'


def get_locus_by_taxon(id):  # noqa: E501
    """Returns all phenotypes for a germplasm that we have

     # noqa: E501

    :param id: Unique database ID for the taaon
    :type id: str

    :rtype: List[Locus]
    """
    return 'do some magic!'


def get_qt_ls():  # noqa: E501
    """Returns all the QTLs (Quantitative Trait Loci) we have

     # noqa: E501


    :rtype: List[QTL]
    """
    return 'do some magic!'


def get_qtl_by_germplasm_trait(germplasmId, traitId):  # noqa: E501
    """Returns all phenotypes for a germplasm that we have

     # noqa: E501

    :param germplasmId: Unique database ID for the germplasm
    :type germplasmId: str
    :param traitId: Unique database ID for the trait in question
    :type traitId: str

    :rtype: List[QTL]
    """
    return 'do some magic!'


def get_taxonomy():  # noqa: E501
    """Returns all germplasm we have

     # noqa: E501


    :rtype: List[Taxonomy]
    """
    return 'do some magic!'


def get_taxonomy_by_id(id):  # noqa: E501
    """Returns all germplasm we have

     # noqa: E501

    :param id: Unique database ID for the taxonomy
    :type id: str

    :rtype: Taxonomy
    """
    return 'do some magic!'


def get_traits():  # noqa: E501
    """Returns all phenotypes we have

     # noqa: E501


    :rtype: List[Phenotype]
    """
    return 'do some magic!'


def get_traits_by_germplasm(germplasmId):  # noqa: E501
    """Returns all phenotypes for a germplasm that we have

     # noqa: E501

    :param germplasmId: Unique database ID for the germplasm
    :type germplasmId: str

    :rtype: List[Phenotype]
    """
    return 'do some magic!'
