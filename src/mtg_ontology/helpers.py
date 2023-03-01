import json
from pathlib import Path
from typing import Dict, Any

from linkml.generators.owlgen import MetadataProfile, OwlSchemaGenerator
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.dumpers import rdflib_dumper
from rdflib import Graph
from tempfile import NamedTemporaryFile

SCHEMA_PATH = str(Path(__file__).parent / "schema" / "mtg_ontology.yaml")


def load_prefixmap() -> Dict[str, Any]:
    """Load the prefixmap."""
    return SchemaView(SCHEMA_PATH, merge_imports=False).schema.prefixes


def load_schema() -> SchemaView:
    """Load the MTG schema.
    This is a wrapper around linkml_runtime.utils.schemaview.SchemaView
    """
    return SchemaView(SCHEMA_PATH, merge_imports=False)


SCHEMAVIEW = load_schema()
PREFIXMAP = load_prefixmap()


def instance_to_graph(
    instance, prefixmap=PREFIXMAP, schemaview=SCHEMAVIEW
) -> Graph:
    return rdflib_dumper.as_rdf_graph(
        instance, prefix_map=prefixmap, schemaview=schemaview
    )


def load_schema_rdflib_graph() -> Graph:
    """Load the MTG ontology schema as an RDFLib Graph."""
    metadata_profile = MetadataProfile.linkml
    schema = OwlSchemaGenerator(SCHEMA_PATH, metadata_profile=metadata_profile)
    ttl = NamedTemporaryFile()
    schema.serialize(format="owl", output=ttl.name)
    graph = Graph().parse(ttl.name, format="ttl")
    return graph
