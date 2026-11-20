"""Cell Ontology helpers built on cellxgene-ontology-guide.

Typical use:
    from celltype_rel.ontology import label, depth, relation
    label("CL:0000236")                     # 'B cell'
    depth("CL:0000236")                     # number of ancestors (higher = more specific)
    relation("CL:0000236", "CL:0000787")    # 'compatible' (memory B cell is a kind of B cell)
"""
from functools import lru_cache

from cellxgene_ontology_guide.ontology_parser import OntologyParser


@lru_cache(maxsize=1)
def parser() -> OntologyParser:
    return OntologyParser()


@lru_cache(maxsize=None)
def label(term_id: str) -> str:
    return parser().get_term_label(term_id)


@lru_cache(maxsize=None)
def ancestors(term_id: str) -> frozenset:
    return frozenset(parser().get_term_ancestors(term_id))


def depth(term_id: str) -> int:
    """Number of ancestors: a simple proxy for how specific a label is."""
    return len(ancestors(term_id))


def relation(pred: str, true: str) -> str:
    """Compare two CL terms.

    'exact'      same term
    'compatible' one is an ancestor of the other (a granularity difference)
    'conflict'   neither contains the other (a real disagreement)
    """
    if pred == true:
        return "exact"
    if pred in ancestors(true) or true in ancestors(pred):
        return "compatible"
    return "conflict"


def lowest_common_ancestor(a: str, b: str) -> list[str]:
    """Most specific shared parent term(s) of two CL terms."""
    return parser().get_lowest_common_ancestors(a, b)
