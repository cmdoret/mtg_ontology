import os
import json
import glob
import unittest
from pathlib import Path

from mtg_ontology.helpers import load_prefixmap, load_schema, instance_to_graph
from mtg_ontology.datamodel import Instant, MTGO
from rdflib import Graph
from rdflib.namespace import RDF

ROOT = Path(os.path.join(os.path.dirname(__file__), ".."))

DATA_DIR = Path(ROOT) / "src" / "data" / "examples"


class TestSchema(unittest.TestCase):
    """Test schema utilities."""

    def test_load_prefixmap(self):
        prefixmap = load_prefixmap()

        assert isinstance(prefixmap, dict)
        assert 'mtgo' in prefixmap

    def test_load_schema(self):
        schema = load_schema()

    def test_instance_to_graph(self):
        card = Instant(
            id=str(MTGO.test_instant),
            name='test-instant',
            color='red',
            type_line='instant',
            card_type='instant'
        )
        g = instance_to_graph(card)
        assert isinstance(g, Graph)
        type_triple = [x for x in g.triples((None, RDF.type, None))]
        assert len(type_triple) == 1
        assert str(type_triple[0][2]) == 'mtg:Instant'

        
