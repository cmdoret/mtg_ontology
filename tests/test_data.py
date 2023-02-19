"""Data test."""
import os
import json
import glob
import unittest
from pathlib import Path

from linkml_runtime.loaders import rdf_loader, yaml_loader
from mtg_ontology.datamodel import Card, Creature

ROOT = Path(os.path.join(os.path.dirname(__file__), '..'))

DATA_DIR =  Path(ROOT) / 'src' / 'data' / 'examples'

class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_yaml_cards(self):
        """Data test."""
        for path in DATA_DIR.glob('Card*.yaml'):
            obj = yaml_loader.load(str(path), target_class=Card)
            assert obj
