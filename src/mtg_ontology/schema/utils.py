import json
from pathlib import Path
from typing import Dict, Any

from linkml_runtime.utils.schemaview import SchemaView
from rdflib import Graph

PROJECT_DIR = Path(__file__).parents[3] / "project"


def load_prefixmap() -> Dict[str, Any]:
    """Load the prefixmap."""
    prefixmap_path = PROJECT_DIR / "prefixmap" / "mtg_ontology.yaml"
    with open(prefixmap_path) as pref:
        return json.load(pref)


def load_schema() -> SchemaView:
    """Load the MTG schema.
    This is a wrapper around linkml_runtime.utils.schemaview.SchemaView
    """
    schema_path = str(Path(__file__).parent / "mtg_ontology.yaml")
    return SchemaView(schema_path, merge_imports=False)


def load_ontology_graph() -> Graph:
    """Parse the owl ontology graph using rdflib."""
    graph = Graph()
    owl_path = PROJECT_DIR / "owl" / "mtg_ontology.owl.ttl"
    graph.parse(owl_path, format='ttl')
    return graph
