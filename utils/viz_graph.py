from functools import reduce
import rdflib
from rdflib.namespace import RDFS

from mtg_ontology.datamodel import LINKML
from mtg_ontology.helpers import load_schema_rdflib_graph

schema = load_schema_rdflib_graph()

all_classes = set(
    filter(
        lambda x: isinstance(x, rdflib.term.URIRef),
        reduce(lambda x, y: x + y, schema.subject_objects(RDFS.subClassOf)),
    )
)

select_pred = [
    "rdfs:subClassOf",
    "linkml:permissible_values",
    "rdfs:range",
]
