from functools import reduce
import matplotlib.pyplot as plt
import networkx as nx
import rdflib
from rdflib.namespace import Namespace, OWL, RDF, RDFS
from rdflib.namespace._SKOS import SKOS
from rdflib.term import URIRef
from mtg_ontology.datamodel import LINKML, MTGO
from mtg_ontology.helpers import load_schema_rdflib_graph, SCHEMAVIEW

schema = load_schema_rdflib_graph()

all_classes = set(schema.subjects(RDF.type, Namespace(LINKML).ClassDefinition))
SCHEMAVIEW.slot_descendants

selected_classes = [
    "Ability",
    "Card",
    "Cost",
    "Permanent",
    "Player",
    "RuleStatement",
    "Token",
]

g = rdflib.Graph()
for entity in selected_classes:
    subject = SCHEMAVIEW.get_class(entity)
    predicates = SCHEMAVIEW.class_slots(subject.name)
    if subject is None:
        continue
    print(subject.name, subject.class_uri)
    for pred_name in predicates:
        pred = SCHEMAVIEW.get_slot(pred_name)
        objects = SCHEMAVIEW.slot_range_as_union(pred)
        if pred is None:
            continue
        print(pred.name, pred.slot_uri)
        for obj_name in objects:
            obj = SCHEMAVIEW.get_class(obj_name)
            if obj_name not in selected_classes:
                continue
            print(obj.name, obj.class_uri)
            print('---'*10)
            g.add((URIRef(subject.class_uri), URIRef(pred.name), URIRef(obj.class_uri)))
print(g.serialize(format='nt'))