from functools import reduce
import rdflib
from rdflib.namespace import Namespace, OWL, RDF, RDFS

from mtg_ontology.datamodel import LINKML
from mtg_ontology.helpers import load_schema_rdflib_graph

schema = load_schema_rdflib_graph()

all_classes = set(schema.subjects(RDF.type, Namespace(LINKML).ClassDefinition))
[(s, p, o) for s, p, o in schema if (s in all_classes) and (o in all_classes)]


result = schema.query("""
CONSTRUCT {?s ?p ?o}
WHERE {
    ?s a linkml:ClassDefinition .
    {
        ?s rdfs:subClassOf ?o .
    }
    UNION
    {
        ?class rdfs:subClassOf ?blank .
        ?blank owl:onProperty ?p ;
            owl:allValuesFrom|owl:someValuesFrom ?o .
    }
    ?o a linkml:ClassDefinition .
}
""", initNs={"linkml": LINKML, "owl": OWL, 'rdfs': RDFS})
g = rdflib.Graph().parse(data=result.serialize(format='turtle'))

# convert graph to networkx
import networkx as nx
G = nx.DiGraph()
for s, p, o in g:
    if 'subClassOf' not in p:
        G.add_edge(str(s).split('/')[-1], str(o).split('/')[-1])
# Visualize networkx graph
import matplotlib.pyplot as plt
plt.figure(figsize=(20, 20))
pos = nx.spring_layout(G, k=0.3, iterations=20)
nx.draw_networkx_nodes(G, pos, node_size=100, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='grey', arrowsize=20, arrowstyle='->')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
plt.axis('off')
plt.show()
