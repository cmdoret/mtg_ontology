"""Data test."""
import os
import json
import glob
import unittest
from pathlib import Path

from linkml_runtime.loaders import rdf_loader, yaml_loader
from mtg_ontology.datamodel import (
    AbilityCollection,
    CardCollection,
)

ROOT = Path(os.path.join(os.path.dirname(__file__), ".."))

DATA_DIR = Path(ROOT) / "src" / "data" / "examples"


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_yaml_cards(self):
        """Data test."""
        for path in DATA_DIR.glob("Card*.yaml"):
            obj = yaml_loader.load(str(path), target_class=CardCollection)
            assert obj

    def test_yaml_abilities(self):
        """Data test."""
        for path in DATA_DIR.glob("Ability*.yaml"):
            obj = yaml_loader.load(str(path), target_class=AbilityCollection)
            assert obj

    def test_land_cards(self):
        assert yaml_loader.load(
            str(DATA_DIR / "lands" / "cards.yaml"), target_class=CardCollection
        )

    def test_land_abilities(self):
        assert yaml_loader.load(
            str(DATA_DIR / "lands" / "abilities.yaml"),
            target_class=AbilityCollection,
        )
