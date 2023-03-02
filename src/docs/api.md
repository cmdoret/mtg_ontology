# mtg-ontology


Python dataclasses are generated for each class in the ontology. They can be used to load or dump instances for various tasks.


```yaml title="plains.yaml"
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
from mtg_ontology.datamodel import Land
from mtg_ontology.helpers import instance_to_graph 

plains = yaml_loader.load('plains.yaml', target_class=Land)
island_graph = instance_to_graph(plains)
print(plains_graph.serialize(format='ttl'))
```

```turtle
@prefix example1: <http://www.example.org/rdf#> .
@prefix mtgo1: <https://cmdoret.net/mtg_ontology/> .
@prefix schema1: <http://schema.org/> .

example1:plains a <mtg:Land> ;
    schema1:name "Plains" ;
    mtgo1:artist "Titus Lunter" ;
    mtgo1:card_set "Adventures in the Forgotten Realms" ;
    mtgo1:card_subtype "Plains" ;
    mtgo1:card_supertype "Basic" ;
    mtgo1:card_type "Land" ;
    mtgo1:color <https://mtg.fandom.com/wiki/white> ;
    mtgo1:flavor_text "Searching for a vanished caravan that was bound for Silverymoon, you’ve come to a bank of mysterious fog." ;
    mtgo1:rarity <https://mtg.fandom.com/wiki/common> ;
    mtgo1:type_line "Basic Land - Plains" .
```

The whole (owl) schema can also be loaded into rdflib using:

```python
from mtg_ontology.helpers import load_schema_rdflib_graph
mtgo_graph = load_schema_rdflib_graph()
```
