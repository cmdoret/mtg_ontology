import re
from functools import reduce
import matplotlib.pyplot as plt
import networkx as nx
import rdflib
from rdflib.namespace import Namespace, OWL, RDF, RDFS
from rdflib.namespace._SKOS import SKOS
from rdflib.term import Literal, URIRef
from mtg_ontology.datamodel import LINKML, MTGO
from mtg_ontology.helpers import load_schema_rdflib_graph, SCHEMAVIEW
from urllib.parse import urlsplit

schema = load_schema_rdflib_graph()

all_classes = set(schema.subjects(RDF.type, Namespace(LINKML).ClassDefinition))
SV = SCHEMAVIEW

selected_classes = [
    "Ability",
    "ActivatedAbility",
    "Card",
    "Cost",
    "Permanent",
    "Player",
    "RuleStatement",
    "Token",
]


def class_to_classes(cls: str) -> rdflib.Graph:
    subject = SV.get_class(cls)
    G = rdflib.Graph()
    if subject is None:
        return G
    predicates = SV.class_slots(subject.name)
    for pred_name in predicates:
        pred = SV.get_slot(pred_name)
        objects = SV.slot_range_as_union(pred)
        if pred is None:
            continue
        for obj_name in objects:
            obj = SV.get_class(obj_name)
            if obj is None:
                continue
            G.add(
                (
                    URIRef(subject.class_uri),
                    URIRef(pred.name),
                    URIRef(obj.class_uri),
                )
            )
    return G


def make_uri(obj) -> str:
    return f"{obj.from_schema}/{obj.name}"


def class_to_enums(cls: str) -> rdflib.Graph:
    subject = SV.get_class(cls)
    G = rdflib.Graph()
    if subject is None:
        return G
    slots = map(SV.get_slot, SV.class_slots(subject.name))
    for slot in filter(lambda s: s is not None, slots):
        for target in SV.slot_range_as_union(slot):
            enum = SV.get_enum(target)
            if enum:
                g.add(
                    (
                        URIRef(subject.class_uri),
                        URIRef(make_uri(slot)),
                        URIRef(make_uri(enum)),
                    )
                )
    return G


def class_to_children(cls: str) -> rdflib.Graph:
    s = SCHEMAVIEW.get_class(cls)
    objects = SCHEMAVIEW.get_children(cls)
    G = rdflib.Graph()
    for obj_name in objects:
        o = SCHEMAVIEW.get_class(obj_name)
        G.add((URIRef(s.class_uri), URIRef(LINKML.is_a), URIRef(o.class_uri)))
    return G


g = rdflib.Graph()
for entity in selected_classes:
    g |= class_to_classes(entity)
    # g |= class_to_children(entity)
    g |= class_to_enums(entity)
print(g.serialize(format="nt"))
nxg = nx.DiGraph()


def frag(uri):
    return re.split(r"[#/]", uri)[-1]


for s, p, o in g:
    nxg.add_node(frag(s))
    nxg.add_node(frag(o))
    nxg.add_edge(frag(s), frag(o), label=frag(p))
pos = nx.spring_layout(nxg, scale=0.3)
nx.draw_networkx_nodes(nxg, pos=pos, node_size=100)
nx.draw_networkx_labels(nxg, pos=pos)
nx.draw_networkx_edges(nxg, pos=pos, arrows=True)
nx.draw_networkx_edge_labels(
    nxg, pos=pos, edge_labels=nx.get_edge_attributes(nxg, "label")
)
plt.show()
