# mtg-ontology

An ontology describing Magic: The Gathering.


The aim of this ontology is to provide a formal description of cards and their abilities. It is built using [linkml](linkml.io), which automatically generates a schema representation in multiple formats (jsonschema, RDF, SQLschema, SHACL, graphQL, ...).

In addition, python dataclasses are generated for each class in the ontology. They can be used to load or dump instances for various tasks.

```yaml
# island.yaml
id: example:plains
name: Plains
color: white
type_line: Basic Land - Plains
card_type: Land
card_subtype: Plains
card_supertype: Basic
artist: Titus Lunter
flavor_text: "Searching for a vanished caravan that was bound for Silverymoon, you’ve come to a bank of mysterious fog."
card_set: Adventures in the Forgotten Realms
rarity: common
```

```python
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import rdflib_dumper
from mtg_ontology.schema.utils import load_prefixmap, load_schema
from mtg_ontology.datamodel import Land

card = yaml_loader.load('island.yaml', target_class=Land)
graph = rdflib_dumper.as_rdf_graph(
    card,
    prefix_map=load_prefixmap(),
    schemaview=load_schema()
)
print(graph.serialize(format='ttl'))
```

```ttl
@prefix example: <http://www.example.org/rdf#> .
@prefix mtgoc: <https://w3id.org/cmdoret/mtg-ontology/cards/> .
@prefix schema: <http://schema.org/> .
@prefix wiki: <http://en.wikipedia.org/wiki/> .

example:island a mtgoc:Card ;
    schema:name "Island" ;
    mtgoc:artist "David Alvarez" ;
    mtgoc:card_set "Phyrexia: All Will Be One" ;
    mtgoc:card_subtype "Island" ;
    mtgoc:card_supertype "Basic" ;
    mtgoc:card_type "Land" ;
    mtgoc:color wiki:Q1088 ;
    mtgoc:rarity "common" ;
    mtgoc:type_line "Basic Land - Island" .
```

The whole schema can also be loaded into rdflib using:

```python
from mtg_ontology.schema.utils import load_ontology_graph
mtg_graph = load_ontology_graph()
```