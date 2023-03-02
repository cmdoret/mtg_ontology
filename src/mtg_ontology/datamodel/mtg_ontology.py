# Auto generated from mtg_ontology.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-02T05:41:34
# Schema: mtgo
#
# id: https://cmdoret.net/mtg_ontology/
# description: An ontology describing Magic: The Gathering. It provides the concepts and relationships needed to
#              represent cards, their cost and abilities.
# license: GNU GPL v3.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EXAMPLE = CurieNamespace('example', 'http://www.example.org/rdf#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MTG = CurieNamespace('mtg', 'https://mtg.fandom.com/wiki/')
MTGO = CurieNamespace('mtgo', 'https://cmdoret.net/mtg_ontology/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SCRYFALL = CurieNamespace('scryfall', 'https://api.scryfall.com/cards/')
DEFAULT_ = MTGO


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class ThingId(URIorCURIE):
    pass


class PermanentId(NamedThingId):
    pass


class SpellId(ThingId):
    pass


class TokenId(PermanentId):
    pass


class CardId(NamedThingId):
    pass


class AnyEnchantmentId(PermanentId):
    pass


class AnyCreatureId(PermanentId):
    pass


class AnyArtifactId(PermanentId):
    pass


class SorceryId(CardId):
    pass


class InstantId(CardId):
    pass


class EnchantmentId(CardId):
    pass


class EnchantmentTokenId(TokenId):
    pass


class ArtifactId(CardId):
    pass


class ArtifactTokenId(TokenId):
    pass


class CreatureId(CardId):
    pass


class CreatureTokenId(TokenId):
    pass


class LandId(CardId):
    pass


class CostId(ThingId):
    pass


class ManaId(ThingId):
    pass


class ManaCostId(CostId):
    pass


class LifeCostId(CostId):
    pass


class AbilityId(ThingId):
    pass


class ActivatedAbilityId(AbilityId):
    pass


class StaticAbilityId(AbilityId):
    pass


class TriggeredAbilityId(AbilityId):
    pass


class ConditionId(ThingId):
    pass


class SpecificationId(ThingId):
    pass


class ActionSpecificationId(SpecificationId):
    pass


class ValueSpecificationId(SpecificationId):
    pass


class TimeSpecificationId(ThingId):
    pass


class CounterId(ThingId):
    pass


class PowerToughnessCounterId(CounterId):
    pass


class KeywordCounterId(CounterId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MTGO.NamedThing

    id: Union[str, NamedThingId] = None
    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Thing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = MTGO.Thing

    id: Union[str, ThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Permanent(NamedThing):
    """
    A card or token that can be put onto the battlefield.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Permanent
    class_class_curie: ClassVar[str] = "mtgo:Permanent"
    class_name: ClassVar[str] = "Permanent"
    class_model_uri: ClassVar[URIRef] = MTGO.Permanent

    id: Union[str, PermanentId] = None
    name: str = None

@dataclass
class Spell(Thing):
    """
    An object on the stack. Either a card that has been cast, or a copy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Spell
    class_class_curie: ClassVar[str] = "mtgo:Spell"
    class_name: ClassVar[str] = "Spell"
    class_model_uri: ClassVar[URIRef] = MTGO.Spell

    id: Union[str, SpellId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpellId):
            self.id = SpellId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Token(Permanent):
    """
    A permanent that is not represented by a regular card and does not have a casting cost.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Token
    class_class_curie: ClassVar[str] = "mtgo:Token"
    class_name: ClassVar[str] = "Token"
    class_model_uri: ClassVar[URIRef] = MTGO.Token

    id: Union[str, TokenId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None
    card_set: Optional[str] = None
    ability: Optional[Union[Union[str, AbilityId], List[Union[str, AbilityId]]]] = empty_list()
    artist: Optional[str] = None
    flavor_text: Optional[str] = None
    card_subtype: Optional[Union[str, List[str]]] = empty_list()
    card_supertype: Optional[Union[str, List[str]]] = empty_list()
    oracle_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TokenId):
            self.id = TokenId(self.id)

        if self._is_empty(self.color):
            self.MissingRequiredField("color")
        if not isinstance(self.color, list):
            self.color = [self.color] if self.color is not None else []
        self.color = [v if isinstance(v, Color) else Color(v) for v in self.color]

        if self._is_empty(self.type_line):
            self.MissingRequiredField("type_line")
        if not isinstance(self.type_line, str):
            self.type_line = str(self.type_line)

        if self._is_empty(self.card_type):
            self.MissingRequiredField("card_type")
        if not isinstance(self.card_type, str):
            self.card_type = str(self.card_type)

        if self.card_set is not None and not isinstance(self.card_set, str):
            self.card_set = str(self.card_set)

        if not isinstance(self.ability, list):
            self.ability = [self.ability] if self.ability is not None else []
        self.ability = [v if isinstance(v, AbilityId) else AbilityId(v) for v in self.ability]

        if self.artist is not None and not isinstance(self.artist, str):
            self.artist = str(self.artist)

        if self.flavor_text is not None and not isinstance(self.flavor_text, str):
            self.flavor_text = str(self.flavor_text)

        if not isinstance(self.card_subtype, list):
            self.card_subtype = [self.card_subtype] if self.card_subtype is not None else []
        self.card_subtype = [v if isinstance(v, str) else str(v) for v in self.card_subtype]

        if not isinstance(self.card_supertype, list):
            self.card_supertype = [self.card_supertype] if self.card_supertype is not None else []
        self.card_supertype = [v if isinstance(v, str) else str(v) for v in self.card_supertype]

        if self.oracle_text is not None and not isinstance(self.oracle_text, str):
            self.oracle_text = str(self.oracle_text)

        super().__post_init__(**kwargs)


@dataclass
class Card(NamedThing):
    """
    A card in the Magic The Gathering game.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Card
    class_class_curie: ClassVar[str] = "mtgo:Card"
    class_name: ClassVar[str] = "Card"
    class_model_uri: ClassVar[URIRef] = MTGO.Card

    id: Union[str, CardId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None
    mana_cost: Optional[Union[Union[str, ManaCostId], List[Union[str, ManaCostId]]]] = empty_list()
    converted_mana_cost: Optional[int] = None
    card_set: Optional[str] = None
    ability: Optional[Union[Union[str, AbilityId], List[Union[str, AbilityId]]]] = empty_list()
    artist: Optional[str] = None
    flavor_text: Optional[str] = None
    card_subtype: Optional[Union[str, List[str]]] = empty_list()
    card_supertype: Optional[Union[str, List[str]]] = empty_list()
    rarity: Optional[Union[str, "Rarity"]] = None
    oracle_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.color):
            self.MissingRequiredField("color")
        if not isinstance(self.color, list):
            self.color = [self.color] if self.color is not None else []
        self.color = [v if isinstance(v, Color) else Color(v) for v in self.color]

        if self._is_empty(self.type_line):
            self.MissingRequiredField("type_line")
        if not isinstance(self.type_line, str):
            self.type_line = str(self.type_line)

        if self._is_empty(self.card_type):
            self.MissingRequiredField("card_type")
        if not isinstance(self.card_type, str):
            self.card_type = str(self.card_type)

        if not isinstance(self.mana_cost, list):
            self.mana_cost = [self.mana_cost] if self.mana_cost is not None else []
        self.mana_cost = [v if isinstance(v, ManaCostId) else ManaCostId(v) for v in self.mana_cost]

        if self.converted_mana_cost is not None and not isinstance(self.converted_mana_cost, int):
            self.converted_mana_cost = int(self.converted_mana_cost)

        if self.card_set is not None and not isinstance(self.card_set, str):
            self.card_set = str(self.card_set)

        if not isinstance(self.ability, list):
            self.ability = [self.ability] if self.ability is not None else []
        self.ability = [v if isinstance(v, AbilityId) else AbilityId(v) for v in self.ability]

        if self.artist is not None and not isinstance(self.artist, str):
            self.artist = str(self.artist)

        if self.flavor_text is not None and not isinstance(self.flavor_text, str):
            self.flavor_text = str(self.flavor_text)

        if not isinstance(self.card_subtype, list):
            self.card_subtype = [self.card_subtype] if self.card_subtype is not None else []
        self.card_subtype = [v if isinstance(v, str) else str(v) for v in self.card_subtype]

        if not isinstance(self.card_supertype, list):
            self.card_supertype = [self.card_supertype] if self.card_supertype is not None else []
        self.card_supertype = [v if isinstance(v, str) else str(v) for v in self.card_supertype]

        if self.rarity is not None and not isinstance(self.rarity, Rarity):
            self.rarity = Rarity(self.rarity)

        if self.oracle_text is not None and not isinstance(self.oracle_text, str):
            self.oracle_text = str(self.oracle_text)

        super().__post_init__(**kwargs)


@dataclass
class AnyEnchantment(Permanent):
    """
    A permanent which applies persistent magical effects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.AnyEnchantment
    class_class_curie: ClassVar[str] = "mtgo:AnyEnchantment"
    class_name: ClassVar[str] = "AnyEnchantment"
    class_model_uri: ClassVar[URIRef] = MTGO.AnyEnchantment

    id: Union[str, AnyEnchantmentId] = None
    name: str = None

@dataclass
class AnyCreature(Permanent):
    """
    A creature that can be summoned to the battlefield.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.AnyCreature
    class_class_curie: ClassVar[str] = "mtgo:AnyCreature"
    class_name: ClassVar[str] = "AnyCreature"
    class_model_uri: ClassVar[URIRef] = MTGO.AnyCreature

    id: Union[str, AnyCreatureId] = None
    name: str = None
    power: int = None
    toughness: int = None
    variable_power: Optional[Union[bool, Bool]] = None
    variable_toughness: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.power):
            self.MissingRequiredField("power")
        if not isinstance(self.power, int):
            self.power = int(self.power)

        if self._is_empty(self.toughness):
            self.MissingRequiredField("toughness")
        if not isinstance(self.toughness, int):
            self.toughness = int(self.toughness)

        if self.variable_power is not None and not isinstance(self.variable_power, Bool):
            self.variable_power = Bool(self.variable_power)

        if self.variable_toughness is not None and not isinstance(self.variable_toughness, Bool):
            self.variable_toughness = Bool(self.variable_toughness)

        super().__post_init__(**kwargs)


@dataclass
class AnyArtifact(Permanent):
    """
    A permanent representing a magical item, animated construct, or other objects and devices.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.AnyArtifact
    class_class_curie: ClassVar[str] = "mtgo:AnyArtifact"
    class_name: ClassVar[str] = "AnyArtifact"
    class_model_uri: ClassVar[URIRef] = MTGO.AnyArtifact

    id: Union[str, AnyArtifactId] = None
    name: str = None

@dataclass
class Sorcery(Card):
    """
    A card that represents a sorcery spell that can be cast.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Sorcery
    class_class_curie: ClassVar[str] = "mtgo:Sorcery"
    class_name: ClassVar[str] = "Sorcery"
    class_model_uri: ClassVar[URIRef] = MTGO.Sorcery

    id: Union[str, SorceryId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SorceryId):
            self.id = SorceryId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Instant(Card):
    """
    A card that represents an instant spell that can be cast.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Instant
    class_class_curie: ClassVar[str] = "mtgo:Instant"
    class_name: ClassVar[str] = "Instant"
    class_model_uri: ClassVar[URIRef] = MTGO.Instant

    id: Union[str, InstantId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstantId):
            self.id = InstantId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Enchantment(Card):
    """
    A card that represents an enchantment that can be cast and put onto the battlefield.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Enchantment
    class_class_curie: ClassVar[str] = "mtgo:Enchantment"
    class_name: ClassVar[str] = "Enchantment"
    class_model_uri: ClassVar[URIRef] = MTGO.Enchantment

    id: Union[str, EnchantmentId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnchantmentId):
            self.id = EnchantmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnchantmentToken(Token):
    """
    A token that represents an enchantment that can be placed onto the battlefield by other effects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.EnchantmentToken
    class_class_curie: ClassVar[str] = "mtgo:EnchantmentToken"
    class_name: ClassVar[str] = "EnchantmentToken"
    class_model_uri: ClassVar[URIRef] = MTGO.EnchantmentToken

    id: Union[str, EnchantmentTokenId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnchantmentTokenId):
            self.id = EnchantmentTokenId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Artifact(Card):
    """
    A card that represents an artifact that can be cast and put onto the battlefield.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Artifact
    class_class_curie: ClassVar[str] = "mtgo:Artifact"
    class_name: ClassVar[str] = "Artifact"
    class_model_uri: ClassVar[URIRef] = MTGO.Artifact

    id: Union[str, ArtifactId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArtifactId):
            self.id = ArtifactId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ArtifactToken(Token):
    """
    A token that represents an artifact that can be placed onto the battlefield by other effects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.ArtifactToken
    class_class_curie: ClassVar[str] = "mtgo:ArtifactToken"
    class_name: ClassVar[str] = "ArtifactToken"
    class_model_uri: ClassVar[URIRef] = MTGO.ArtifactToken

    id: Union[str, ArtifactTokenId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArtifactTokenId):
            self.id = ArtifactTokenId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Creature(Card):
    """
    A card that represents a creature that can be cast and put onto the battlefield.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Creature
    class_class_curie: ClassVar[str] = "mtgo:Creature"
    class_name: ClassVar[str] = "Creature"
    class_model_uri: ClassVar[URIRef] = MTGO.Creature

    id: Union[str, CreatureId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None
    power: int = None
    toughness: int = None
    variable_power: Optional[Union[bool, Bool]] = None
    variable_toughness: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CreatureId):
            self.id = CreatureId(self.id)

        if self._is_empty(self.power):
            self.MissingRequiredField("power")
        if not isinstance(self.power, int):
            self.power = int(self.power)

        if self._is_empty(self.toughness):
            self.MissingRequiredField("toughness")
        if not isinstance(self.toughness, int):
            self.toughness = int(self.toughness)

        if self.variable_power is not None and not isinstance(self.variable_power, Bool):
            self.variable_power = Bool(self.variable_power)

        if self.variable_toughness is not None and not isinstance(self.variable_toughness, Bool):
            self.variable_toughness = Bool(self.variable_toughness)

        super().__post_init__(**kwargs)


@dataclass
class CreatureToken(Token):
    """
    A token that represents a creature that can be placed onto the battlefield by other effects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.CreatureToken
    class_class_curie: ClassVar[str] = "mtgo:CreatureToken"
    class_name: ClassVar[str] = "CreatureToken"
    class_model_uri: ClassVar[URIRef] = MTGO.CreatureToken

    id: Union[str, CreatureTokenId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None
    power: int = None
    toughness: int = None
    variable_power: Optional[Union[bool, Bool]] = None
    variable_toughness: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CreatureTokenId):
            self.id = CreatureTokenId(self.id)

        if self._is_empty(self.power):
            self.MissingRequiredField("power")
        if not isinstance(self.power, int):
            self.power = int(self.power)

        if self._is_empty(self.toughness):
            self.MissingRequiredField("toughness")
        if not isinstance(self.toughness, int):
            self.toughness = int(self.toughness)

        if self.variable_power is not None and not isinstance(self.variable_power, Bool):
            self.variable_power = Bool(self.variable_power)

        if self.variable_toughness is not None and not isinstance(self.variable_toughness, Bool):
            self.variable_toughness = Bool(self.variable_toughness)

        super().__post_init__(**kwargs)


@dataclass
class Land(Card):
    """
    A card that represents a land that can be tapped for mana.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Land
    class_class_curie: ClassVar[str] = "mtgo:Land"
    class_name: ClassVar[str] = "Land"
    class_model_uri: ClassVar[URIRef] = MTGO.Land

    id: Union[str, LandId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LandId):
            self.id = LandId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cost(Thing):
    """
    The cost of a card or ability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Cost
    class_class_curie: ClassVar[str] = "mtgo:Cost"
    class_name: ClassVar[str] = "Cost"
    class_model_uri: ClassVar[URIRef] = MTGO.Cost

    id: Union[str, CostId] = None
    value: Optional[int] = None
    intersection: Optional[Union[str, CostId]] = None
    union: Optional[Union[str, CostId]] = None
    variable_cost: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CostId):
            self.id = CostId(self.id)

        if self.value is not None and not isinstance(self.value, int):
            self.value = int(self.value)

        if self.intersection is not None and not isinstance(self.intersection, CostId):
            self.intersection = CostId(self.intersection)

        if self.union is not None and not isinstance(self.union, CostId):
            self.union = CostId(self.union)

        if self.variable_cost is not None and not isinstance(self.variable_cost, Bool):
            self.variable_cost = Bool(self.variable_cost)

        super().__post_init__(**kwargs)


@dataclass
class Mana(Thing):
    """
    A mana in the pool.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Mana
    class_class_curie: ClassVar[str] = "mtgo:Mana"
    class_name: ClassVar[str] = "Mana"
    class_model_uri: ClassVar[URIRef] = MTGO.Mana

    id: Union[str, ManaId] = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    snow: Optional[Union[bool, Bool]] = None
    phyrexian: Optional[Union[bool, Bool]] = None
    hybrid: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManaId):
            self.id = ManaId(self.id)

        if self._is_empty(self.color):
            self.MissingRequiredField("color")
        if not isinstance(self.color, list):
            self.color = [self.color] if self.color is not None else []
        self.color = [v if isinstance(v, Color) else Color(v) for v in self.color]

        if self.snow is not None and not isinstance(self.snow, Bool):
            self.snow = Bool(self.snow)

        if self.phyrexian is not None and not isinstance(self.phyrexian, Bool):
            self.phyrexian = Bool(self.phyrexian)

        if self.hybrid is not None and not isinstance(self.hybrid, Bool):
            self.hybrid = Bool(self.hybrid)

        super().__post_init__(**kwargs)


@dataclass
class ManaCost(Cost):
    """
    The mana cost of a card or ability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.ManaCost
    class_class_curie: ClassVar[str] = "mtgo:ManaCost"
    class_name: ClassVar[str] = "ManaCost"
    class_model_uri: ClassVar[URIRef] = MTGO.ManaCost

    id: Union[str, ManaCostId] = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    snow: Optional[Union[bool, Bool]] = None
    phyrexian: Optional[Union[bool, Bool]] = None
    hybrid: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManaCostId):
            self.id = ManaCostId(self.id)

        if self._is_empty(self.color):
            self.MissingRequiredField("color")
        if not isinstance(self.color, list):
            self.color = [self.color] if self.color is not None else []
        self.color = [v if isinstance(v, Color) else Color(v) for v in self.color]

        if self.snow is not None and not isinstance(self.snow, Bool):
            self.snow = Bool(self.snow)

        if self.phyrexian is not None and not isinstance(self.phyrexian, Bool):
            self.phyrexian = Bool(self.phyrexian)

        if self.hybrid is not None and not isinstance(self.hybrid, Bool):
            self.hybrid = Bool(self.hybrid)

        super().__post_init__(**kwargs)


@dataclass
class LifeCost(Cost):
    """
    The life cost of a card or ability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.LifeCost
    class_class_curie: ClassVar[str] = "mtgo:LifeCost"
    class_name: ClassVar[str] = "LifeCost"
    class_model_uri: ClassVar[URIRef] = MTGO.LifeCost

    id: Union[str, LifeCostId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LifeCostId):
            self.id = LifeCostId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CardCollection(YAMLRoot):
    """
    A collection of cards and associated costs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.CardCollection
    class_class_curie: ClassVar[str] = "mtgo:CardCollection"
    class_name: ClassVar[str] = "CardCollection"
    class_model_uri: ClassVar[URIRef] = MTGO.CardCollection

    cards: Optional[Union[Dict[Union[str, CardId], Union[dict, Card]], List[Union[dict, Card]]]] = empty_dict()
    costs: Optional[Union[Dict[Union[str, CostId], Union[dict, Cost]], List[Union[dict, Cost]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="cards", slot_type=Card, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="costs", slot_type=Cost, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Ability(Thing):
    """
    A card ability, activated, triggered or static.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Ability
    class_class_curie: ClassVar[str] = "mtgo:Ability"
    class_name: ClassVar[str] = "Ability"
    class_model_uri: ClassVar[URIRef] = MTGO.Ability

    id: Union[str, AbilityId] = None
    rules_text: Optional[str] = None
    effect: Optional[Union[str, ConditionId]] = None
    ability_keyword: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.rules_text is not None and not isinstance(self.rules_text, str):
            self.rules_text = str(self.rules_text)

        if self.effect is not None and not isinstance(self.effect, ConditionId):
            self.effect = ConditionId(self.effect)

        if self.ability_keyword is not None and not isinstance(self.ability_keyword, str):
            self.ability_keyword = str(self.ability_keyword)

        super().__post_init__(**kwargs)


@dataclass
class ActivatedAbility(Ability):
    """
    A card ability which can be activated for a cost.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.ActivatedAbility
    class_class_curie: ClassVar[str] = "mtgo:ActivatedAbility"
    class_name: ClassVar[str] = "ActivatedAbility"
    class_model_uri: ClassVar[URIRef] = MTGO.ActivatedAbility

    id: Union[str, ActivatedAbilityId] = None
    cost: Optional[Union[str, List[str]]] = empty_list()
    condition: Optional[Union[str, ConditionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivatedAbilityId):
            self.id = ActivatedAbilityId(self.id)

        if not isinstance(self.cost, list):
            self.cost = [self.cost] if self.cost is not None else []
        self.cost = [v if isinstance(v, str) else str(v) for v in self.cost]

        if self.condition is not None and not isinstance(self.condition, ConditionId):
            self.condition = ConditionId(self.condition)

        super().__post_init__(**kwargs)


@dataclass
class StaticAbility(Ability):
    """
    A card ability which remains active until endgame once put into effect.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.StaticAbility
    class_class_curie: ClassVar[str] = "mtgo:StaticAbility"
    class_name: ClassVar[str] = "StaticAbility"
    class_model_uri: ClassVar[URIRef] = MTGO.StaticAbility

    id: Union[str, StaticAbilityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StaticAbilityId):
            self.id = StaticAbilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TriggeredAbility(Ability):
    """
    A card ability, triggered by an event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.TriggeredAbility
    class_class_curie: ClassVar[str] = "mtgo:TriggeredAbility"
    class_name: ClassVar[str] = "TriggeredAbility"
    class_model_uri: ClassVar[URIRef] = MTGO.TriggeredAbility

    id: Union[str, TriggeredAbilityId] = None
    condition: Optional[Union[str, ConditionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TriggeredAbilityId):
            self.id = TriggeredAbilityId(self.id)

        if self.condition is not None and not isinstance(self.condition, ConditionId):
            self.condition = ConditionId(self.condition)

        super().__post_init__(**kwargs)


@dataclass
class Condition(Thing):
    """
    A condition expressed as constraints.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Condition
    class_class_curie: ClassVar[str] = "mtgo:Condition"
    class_name: ClassVar[str] = "Condition"
    class_model_uri: ClassVar[URIRef] = MTGO.Condition

    id: Union[str, ConditionId] = None
    source: Optional[str] = None
    target: Optional[str] = None
    action_spec: Optional[Union[Union[str, ActionSpecificationId], List[Union[str, ActionSpecificationId]]]] = empty_list()
    value_spec: Optional[Union[Union[str, ValueSpecificationId], List[Union[str, ValueSpecificationId]]]] = empty_list()
    time_spec: Optional[Union[Union[str, TimeSpecificationId], List[Union[str, TimeSpecificationId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConditionId):
            self.id = ConditionId(self.id)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.target is not None and not isinstance(self.target, str):
            self.target = str(self.target)

        if not isinstance(self.action_spec, list):
            self.action_spec = [self.action_spec] if self.action_spec is not None else []
        self.action_spec = [v if isinstance(v, ActionSpecificationId) else ActionSpecificationId(v) for v in self.action_spec]

        if not isinstance(self.value_spec, list):
            self.value_spec = [self.value_spec] if self.value_spec is not None else []
        self.value_spec = [v if isinstance(v, ValueSpecificationId) else ValueSpecificationId(v) for v in self.value_spec]

        if not isinstance(self.time_spec, list):
            self.time_spec = [self.time_spec] if self.time_spec is not None else []
        self.time_spec = [v if isinstance(v, TimeSpecificationId) else TimeSpecificationId(v) for v in self.time_spec]

        super().__post_init__(**kwargs)


@dataclass
class AbilityCollection(YAMLRoot):
    """
    A collection of abilities and associated concepts.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.AbilityCollection
    class_class_curie: ClassVar[str] = "mtgo:AbilityCollection"
    class_name: ClassVar[str] = "AbilityCollection"
    class_model_uri: ClassVar[URIRef] = MTGO.AbilityCollection

    activated_abilities: Optional[Union[Dict[Union[str, ActivatedAbilityId], Union[dict, ActivatedAbility]], List[Union[dict, ActivatedAbility]]]] = empty_dict()
    conditions: Optional[Union[Dict[Union[str, ConditionId], Union[dict, Condition]], List[Union[dict, Condition]]]] = empty_dict()
    mana_costs: Optional[Union[Dict[Union[str, ManaCostId], Union[dict, ManaCost]], List[Union[dict, ManaCost]]]] = empty_dict()
    value_specifications: Optional[Union[Dict[Union[str, ValueSpecificationId], Union[dict, "ValueSpecification"]], List[Union[dict, "ValueSpecification"]]]] = empty_dict()
    action_specifications: Optional[Union[Dict[Union[str, ActionSpecificationId], Union[dict, "ActionSpecification"]], List[Union[dict, "ActionSpecification"]]]] = empty_dict()
    time_specifications: Optional[Union[Dict[Union[str, TimeSpecificationId], Union[dict, "TimeSpecification"]], List[Union[dict, "TimeSpecification"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="activated_abilities", slot_type=ActivatedAbility, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="conditions", slot_type=Condition, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="mana_costs", slot_type=ManaCost, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="value_specifications", slot_type=ValueSpecification, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="action_specifications", slot_type=ActionSpecification, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="time_specifications", slot_type=TimeSpecification, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Specification(Thing):
    """
    A specification for a thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Specification
    class_class_curie: ClassVar[str] = "mtgo:Specification"
    class_name: ClassVar[str] = "Specification"
    class_model_uri: ClassVar[URIRef] = MTGO.Specification

    id: Union[str, SpecificationId] = None
    constraint: Optional[str] = None
    intersection: Optional[Union[str, NamedThingId]] = None
    union: Optional[Union[str, NamedThingId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.constraint is not None and not isinstance(self.constraint, str):
            self.constraint = str(self.constraint)

        if self.intersection is not None and not isinstance(self.intersection, NamedThingId):
            self.intersection = NamedThingId(self.intersection)

        if self.union is not None and not isinstance(self.union, NamedThingId):
            self.union = NamedThingId(self.union)

        super().__post_init__(**kwargs)


@dataclass
class ActionSpecification(Specification):
    """
    A specification for an action.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.ActionSpecification
    class_class_curie: ClassVar[str] = "mtgo:ActionSpecification"
    class_name: ClassVar[str] = "ActionSpecification"
    class_model_uri: ClassVar[URIRef] = MTGO.ActionSpecification

    id: Union[str, ActionSpecificationId] = None
    action: Union[str, "Action"] = None
    intersection: Optional[Union[str, ActionSpecificationId]] = None
    union: Optional[Union[str, ActionSpecificationId]] = None
    constraint: Optional[Union[str, "ActionConstraint"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActionSpecificationId):
            self.id = ActionSpecificationId(self.id)

        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, Action):
            self.action = Action(self.action)

        if self.intersection is not None and not isinstance(self.intersection, ActionSpecificationId):
            self.intersection = ActionSpecificationId(self.intersection)

        if self.union is not None and not isinstance(self.union, ActionSpecificationId):
            self.union = ActionSpecificationId(self.union)

        if self.constraint is not None and not isinstance(self.constraint, ActionConstraint):
            self.constraint = ActionConstraint(self.constraint)

        super().__post_init__(**kwargs)


@dataclass
class ValueSpecification(Specification):
    """
    A specification for a quantitative value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.ValueSpecification
    class_class_curie: ClassVar[str] = "mtgo:ValueSpecification"
    class_name: ClassVar[str] = "ValueSpecification"
    class_model_uri: ClassVar[URIRef] = MTGO.ValueSpecification

    id: Union[str, ValueSpecificationId] = None
    value: Optional[int] = None
    unit: Optional[str] = None
    intersection: Optional[Union[str, ValueSpecificationId]] = None
    union: Optional[Union[str, ValueSpecificationId]] = None
    constraint: Optional[Union[str, "ValueConstraint"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ValueSpecificationId):
            self.id = ValueSpecificationId(self.id)

        if self.value is not None and not isinstance(self.value, int):
            self.value = int(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.intersection is not None and not isinstance(self.intersection, ValueSpecificationId):
            self.intersection = ValueSpecificationId(self.intersection)

        if self.union is not None and not isinstance(self.union, ValueSpecificationId):
            self.union = ValueSpecificationId(self.union)

        if self.constraint is not None and not isinstance(self.constraint, ValueConstraint):
            self.constraint = ValueConstraint(self.constraint)

        super().__post_init__(**kwargs)


@dataclass
class TimeSpecification(Thing):
    """
    A specification for a time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.TimeSpecification
    class_class_curie: ClassVar[str] = "mtgo:TimeSpecification"
    class_name: ClassVar[str] = "TimeSpecification"
    class_model_uri: ClassVar[URIRef] = MTGO.TimeSpecification

    id: Union[str, TimeSpecificationId] = None
    turn_phase: Optional[Union[str, "TurnPhase"]] = None
    player: Optional[Union[str, "Player"]] = None
    intersection: Optional[Union[str, TimeSpecificationId]] = None
    union: Optional[Union[str, TimeSpecificationId]] = None
    constraint: Optional[Union[str, "TimeConstraint"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TimeSpecificationId):
            self.id = TimeSpecificationId(self.id)

        if self.turn_phase is not None and not isinstance(self.turn_phase, TurnPhase):
            self.turn_phase = TurnPhase(self.turn_phase)

        if self.player is not None and not isinstance(self.player, Player):
            self.player = Player(self.player)

        if self.intersection is not None and not isinstance(self.intersection, TimeSpecificationId):
            self.intersection = TimeSpecificationId(self.intersection)

        if self.union is not None and not isinstance(self.union, TimeSpecificationId):
            self.union = TimeSpecificationId(self.union)

        if self.constraint is not None and not isinstance(self.constraint, TimeConstraint):
            self.constraint = TimeConstraint(self.constraint)

        super().__post_init__(**kwargs)


@dataclass
class Counter(Thing):
    """
    A counter, such as a +1/+1 counter.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Counter
    class_class_curie: ClassVar[str] = "mtgo:Counter"
    class_name: ClassVar[str] = "Counter"
    class_model_uri: ClassVar[URIRef] = MTGO.Counter

    id: Union[str, CounterId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CounterId):
            self.id = CounterId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PowerToughnessCounter(Counter):
    """
    A counter that gives a power and toughness modifier to a creature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.PowerToughnessCounter
    class_class_curie: ClassVar[str] = "mtgo:PowerToughnessCounter"
    class_name: ClassVar[str] = "PowerToughnessCounter"
    class_model_uri: ClassVar[URIRef] = MTGO.PowerToughnessCounter

    id: Union[str, PowerToughnessCounterId] = None
    power_modifier: Optional[int] = None
    toughness_modifier: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PowerToughnessCounterId):
            self.id = PowerToughnessCounterId(self.id)

        if self.power_modifier is not None and not isinstance(self.power_modifier, int):
            self.power_modifier = int(self.power_modifier)

        if self.toughness_modifier is not None and not isinstance(self.toughness_modifier, int):
            self.toughness_modifier = int(self.toughness_modifier)

        super().__post_init__(**kwargs)


@dataclass
class KeywordCounter(Counter):
    """
    A counter that gives a some ability to a permanent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.KeywordCounter
    class_class_curie: ClassVar[str] = "mtgo:KeywordCounter"
    class_name: ClassVar[str] = "KeywordCounter"
    class_model_uri: ClassVar[URIRef] = MTGO.KeywordCounter

    id: Union[str, KeywordCounterId] = None
    ability_keyword: Optional[str] = None
    value_spec: Optional[Union[Union[str, ValueSpecificationId], List[Union[str, ValueSpecificationId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeywordCounterId):
            self.id = KeywordCounterId(self.id)

        if self.ability_keyword is not None and not isinstance(self.ability_keyword, str):
            self.ability_keyword = str(self.ability_keyword)

        if not isinstance(self.value_spec, list):
            self.value_spec = [self.value_spec] if self.value_spec is not None else []
        self.value_spec = [v if isinstance(v, ValueSpecificationId) else ValueSpecificationId(v) for v in self.value_spec]

        super().__post_init__(**kwargs)


# Enumerations
class Color(EnumDefinitionImpl):
    """
    A color, such as Black, Blue, Red, Green, White or Colorless. see_also: mtg:color
    """
    black = PermissibleValue(text="black",
                                 description="The color black, associated with darkness.",
                                 meaning=MTG.black)
    blue = PermissibleValue(text="blue",
                               description="The color blue, associated with water.",
                               meaning=MTG.blue)
    green = PermissibleValue(text="green",
                                 description="The color green, associated with nature.",
                                 meaning=MTG.green)
    red = PermissibleValue(text="red",
                             description="The color red, associated with fire.",
                             meaning=MTG.red)
    white = PermissibleValue(text="white",
                                 description="The color white, associated with light.",
                                 meaning=MTG.white)
    colorless = PermissibleValue(text="colorless",
                                         description="Absence of color.",
                                         meaning=MTG.colorless)

    _defn = EnumDefinition(
        name="Color",
        description="A color, such as Black, Blue, Red, Green, White or Colorless. see_also: mtg:color",
    )

class Rarity(EnumDefinitionImpl):
    """
    The rarity of the card, may be one of Common, Uncommon, Rare or Mythic. see_also: mtg:rarity
    """
    common = PermissibleValue(text="common",
                                   description="The lowest rarity level, identified by a black set image.",
                                   meaning=MTG.common)
    uncommon = PermissibleValue(text="uncommon",
                                       description="The second lowest rarity level, identified by a silver set image.",
                                       meaning=MTG.uncommon)
    rare = PermissibleValue(text="rare",
                               description="The second highest rarity level, identified by a golden set image.",
                               meaning=MTG.rare)
    mythic = PermissibleValue(text="mythic",
                                   description="The highest rarity level, identified by a red set image.",
                                   meaning=MTG.mythic_rare)

    _defn = EnumDefinition(
        name="Rarity",
        description="The rarity of the card, may be one of Common, Uncommon, Rare or Mythic. see_also: mtg:rarity",
    )

class Player(EnumDefinitionImpl):
    """
    One or more human players.
    """
    you = PermissibleValue(text="you",
                             description="The focal player.")
    active_player = PermissibleValue(text="active_player",
                                                 description="The player who is currently taking their turn.")
    non_active_player = PermissibleValue(text="non_active_player",
                                                         description="Any player who is not currently taking their turn.")
    defending_player = PermissibleValue(text="defending_player",
                                                       description="The player who is currently defending.")
    attacking_player = PermissibleValue(text="attacking_player",
                                                       description="The player who is currently attacking.")
    owner = PermissibleValue(text="owner",
                                 description="The player who owns a card.")
    controller = PermissibleValue(text="controller",
                                           description="The player who controls an object on the stack.")
    opponent = PermissibleValue(text="opponent",
                                       description="A player playing against the focal player.")
    opponents = PermissibleValue(text="opponents",
                                         description="All players playing against the focal player.")
    players = PermissibleValue(text="players",
                                     description="All players taking part in the game.")

    _defn = EnumDefinition(
        name="Player",
        description="One or more human players.",
    )

class Action(EnumDefinitionImpl):
    """
    An action taken by a player or card.
    """
    activate = PermissibleValue(text="activate",
                                       description="An ability is activated.",
                                       meaning=MTG.activate)
    add_mana = PermissibleValue(text="add_mana",
                                       description="A player adds mana to their mana pool.")
    attach = PermissibleValue(text="attach",
                                   description="An equipment, aura or fortification is moved onto another object or player.",
                                   meaning=MTG.attach)
    cast = PermissibleValue(text="cast",
                               description="A spell is cast and put on the stack.",
                               meaning=MTG.cast)
    control = PermissibleValue(text="control",
                                     description="A player controls a card.",
                                     meaning=MTG.control_and_ownership)
    counter = PermissibleValue(text="counter",
                                     description="A spell or ability is countered.",
                                     meaning=MTG.counter)
    create = PermissibleValue(text="create",
                                   description="A token is put onto the battlefield.",
                                   meaning=MTG.create)
    deal_damage = PermissibleValue(text="deal_damage",
                                             description="Something deals damage to something else.")
    destroy = PermissibleValue(text="destroy",
                                     description="Transfer one or more permanents from the battlefield to their owner's graveyard.",
                                     meaning=MTG.destroy)
    discard = PermissibleValue(text="discard",
                                     description="Transfer one or more cards from the hand to the graveyard.",
                                     meaning=MTG.discard)
    draw = PermissibleValue(text="draw",
                               description="Transfer one or more cards from the library to the hand.",
                               meaning=MTG.draw)
    exchange = PermissibleValue(text="exchange",
                                       description="The control is swapped between two permanents.",
                                       meaning=MTG.exchange)
    exile = PermissibleValue(text="exile",
                                 description="Remove one or more cards from game.",
                                 meaning=MTG.exile)
    fight = PermissibleValue(text="fight",
                                 description="Two cards fight each other.",
                                 meaning=MTG.fight)
    mill = PermissibleValue(text="mill",
                               description="Transfer one or more cards from the library to the graveyard.",
                               meaning=MTG.mill)
    play = PermissibleValue(text="play",
                               description="A card is played as a land or cast as a spell, whichever is appropriate.",
                               meaning=MTG.play)
    reveal = PermissibleValue(text="reveal",
                                   description="A player reveals a card or cards to other players.",
                                   meaning=MTG.reveal)
    sacrifice = PermissibleValue(text="sacrifice",
                                         description="Transfer one or more permanents you control from the battlefield to their owner's graveyard.",
                                         meaning=MTG.sacrifice)
    scry = PermissibleValue(text="scry",
                               description="A player looks at a certain number of cards from the top of their library, and puts them back at the top or bottom of the library in any order.",
                               meaning=MTG.scry)
    search = PermissibleValue(text="search",
                                   description="A player searches their library.",
                                   meaning=MTG.search)
    shuffle = PermissibleValue(text="shuffle",
                                     description="A player shuffles their library.",
                                     meaning=MTG.shuffle)
    tap = PermissibleValue(text="tap",
                             description="A card is tapped.",
                             meaning=MTG.tap)
    untap = PermissibleValue(text="untap",
                                 description="A card is untapped",
                                 meaning=MTG.untap)

    _defn = EnumDefinition(
        name="Action",
        description="An action taken by a player or card.",
    )

class ActionConstraint(EnumDefinitionImpl):

    must = PermissibleValue(text="must",
                               description="The constraint must be met.")
    may = PermissibleValue(text="may",
                             description="The constraint may be met.")
    must_not = PermissibleValue(text="must_not",
                                       description="The constraint must not be met.")
    may_not = PermissibleValue(text="may_not",
                                     description="The constraint may not be met.")

    _defn = EnumDefinition(
        name="ActionConstraint",
    )

class ValueConstraint(EnumDefinitionImpl):

    equal = PermissibleValue(text="equal",
                                 description="The value must be equal to the target.")
    greater_than = PermissibleValue(text="greater_than",
                                               description="The value must be greater than the target.")
    less_than = PermissibleValue(text="less_than",
                                         description="The value must be less than the target.")
    greater_than_or_equal = PermissibleValue(text="greater_than_or_equal",
                                                                 description="The value must be greater than or equal to the target.")
    less_than_or_equal = PermissibleValue(text="less_than_or_equal",
                                                           description="The value must be less than or equal to the target.")
    not_equal = PermissibleValue(text="not_equal",
                                         description="The value must not be equal to the target.")
    between = PermissibleValue(text="between",
                                     description="The value must be between the target and the target2.")
    not_between = PermissibleValue(text="not_between",
                                             description="The value must not be between the target and the target2.")
    is_not = PermissibleValue(text="is_not",
                                   description="The value must not be equivalent to the target.")
    is_one_of = PermissibleValue(text="is_one_of",
                                         description="The value must be one of the target list.")
    is_not_one_of = PermissibleValue(text="is_not_one_of",
                                                 description="The value must not be one of the target list.")

    _defn = EnumDefinition(
        name="ValueConstraint",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "is",
                PermissibleValue(text="is",
                                 description="The value must be equivalent to the target.") )

class TurnPhase(EnumDefinitionImpl):
    """
    A time during the turn.
    """
    beginning_phase = PermissibleValue(text="beginning_phase",
                                                     description="The beginning of the turn.",
                                                     meaning=MTG.beggining_phase)
    untap_step = PermissibleValue(text="untap_step",
                                           description="The untap step.",
                                           meaning=MTG.untap_step)
    upkeep_step = PermissibleValue(text="upkeep_step",
                                             description="The upkeep step.",
                                             meaning=MTG.upkeep_step)
    draw_step = PermissibleValue(text="draw_step",
                                         description="The draw step.",
                                         meaning=MTG.draw_step)
    main_phase = PermissibleValue(text="main_phase",
                                           description="Either main phase.",
                                           meaning=MTG.main_phase)
    pre_combat_main_phase = PermissibleValue(text="pre_combat_main_phase",
                                                                 description="The first main phase.",
                                                                 meaning=MTG.main_phase)
    post_combat_main_phase = PermissibleValue(text="post_combat_main_phase",
                                                                   description="The second main phase.",
                                                                   meaning=MTG.main_phase)
    combat_phase = PermissibleValue(text="combat_phase",
                                               description="The combat phase.",
                                               meaning=MTG.combat_phase)
    beginning_of_combat_step = PermissibleValue(text="beginning_of_combat_step",
                                                                       description="The first step of the combat phase.",
                                                                       meaning=MTG.beginning_of_combat_step)
    declare_attackers_step = PermissibleValue(text="declare_attackers_step",
                                                                   description="The declare attackers step.",
                                                                   meaning=MTG.declare_attackers_step)
    declare_blockers_step = PermissibleValue(text="declare_blockers_step",
                                                                 description="The declare blockers step.",
                                                                 meaning=MTG.declare_blockers_step)
    combat_damage_step = PermissibleValue(text="combat_damage_step",
                                                           description="The combat damage step.",
                                                           meaning=MTG.combat_damage_step)
    end_of_combat_step = PermissibleValue(text="end_of_combat_step",
                                                           description="The end of combat step.",
                                                           meaning=MTG.end_of_combat_step)
    ending_phase = PermissibleValue(text="ending_phase",
                                               description="The end step.",
                                               meaning=MTG.ending_phase)
    cleanup_step = PermissibleValue(text="cleanup_step",
                                               description="The cleanup step.",
                                               meaning=MTG.cleanup_step)
    turn = PermissibleValue(text="turn",
                               description="A player turn.",
                               meaning=MTG.turn)

    _defn = EnumDefinition(
        name="TurnPhase",
        description="A time during the turn.",
    )

class TimeConstraint(EnumDefinitionImpl):
    """
    A constraint on the time of an event.
    """
    before = PermissibleValue(text="before",
                                   description="The event must occur before the target.")
    after = PermissibleValue(text="after",
                                 description="The event must occur after the target.")
    during = PermissibleValue(text="during",
                                   description="The event must occur during the target.")
    next = PermissibleValue(text="next",
                               description="The event must occur next.")
    previous = PermissibleValue(text="previous",
                                       description="The event must have occurred previously.")
    this = PermissibleValue(text="this",
                               description="The event must occur this time.")
    each = PermissibleValue(text="each",
                               description="The event must occur each time.")

    _defn = EnumDefinition(
        name="TimeConstraint",
        description="A constraint on the time of an event.",
    )

class AbilityKeyword(EnumDefinitionImpl):
    """
    A passive ability represented by word that substitutes for a piece of rules text, such as deathtouch or flying.
    """
    deathtouch = PermissibleValue(text="deathtouch",
                                           description="Any amount of damage a source with deathtouch deals to a creature is enough to destroy it.",
                                           meaning=MTG.deathtouch)
    defender = PermissibleValue(text="defender",
                                       description="A creature with defender can't attack.",
                                       meaning=MTG.defender)
    double_strike = PermissibleValue(text="double_strike",
                                                 description="A creature with double strike deals combat damage twice.",
                                                 meaning=MTG.double_strike)
    enchant = PermissibleValue(text="enchant",
                                     description="The enchant ability restricts what an aura spell can target and what an aura can enchant.",
                                     meaning=MTG.enchant)
    equip = PermissibleValue(text="equip",
                                 description="Attach an equipment to a creature you control.",
                                 meaning=MTG.equip)
    first_strike = PermissibleValue(text="first_strike",
                                               description="A creature with first strike deals combat damage before creatures without first strike.",
                                               meaning=MTG.first_strike)
    flash = PermissibleValue(text="flash",
                                 description="A creature with flash can be cast any time you could cast an instant.",
                                 meaning=MTG.flash)
    flying = PermissibleValue(text="flying",
                                   description="A creature with flying can't be blocked except by creatures with flying or reach.",
                                   meaning=MTG.flying)
    haste = PermissibleValue(text="haste",
                                 description="A creature with haste can attack and tap as soon as it comes under your control.",
                                 meaning=MTG.haste)
    hexproof = PermissibleValue(text="hexproof",
                                       description="A creature with hexproof can't be the target of spells or abilities your opponents control.",
                                       meaning=MTG.hexproof)
    indestructible = PermissibleValue(text="indestructible",
                                                   description="A permanent with indestructible can't be destroyed.",
                                                   meaning=MTG.indestructible)
    lifelink = PermissibleValue(text="lifelink",
                                       description="A creature with lifelink deals damage to a creature or player equal to the damage dealt to it.",
                                       meaning=MTG.lifelink)
    menace = PermissibleValue(text="menace",
                                   description="A creature with menace can't be blocked except by two or more creatures.",
                                   meaning=MTG.menace)
    protection = PermissibleValue(text="protection",
                                           description="A creature with protection from a color or a creature type can't be blocked, targeted, dealt damage, enchanted, or equipped by sources of the chosen color or of the chosen type.",
                                           meaning=MTG.protection)
    reach = PermissibleValue(text="reach",
                                 description="A creature with reach can block creatures with flying.",
                                 meaning=MTG.reach)
    trample = PermissibleValue(text="trample",
                                     description="If a creature with trample would assign enough damage to its blockers to destroy them, it assigns the rest of its damage to defending player or planeswalker.",
                                     meaning=MTG.trample)
    vigilance = PermissibleValue(text="vigilance",
                                         description="A creature with vigilance doesn't tap during your untap step.",
                                         meaning=MTG.vigilance)
    ward = PermissibleValue(text="ward",
                               description="Whenever this creature becomes the target of a spell or ability an opponent controls, counter that spell or ability unless its controller pays N. ",
                               meaning=MTG.ward)

    _defn = EnumDefinition(
        name="AbilityKeyword",
        description="A passive ability represented by word that substitutes for a piece of rules text, such as deathtouch or flying.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MTGO.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MTGO.name, domain=None, range=str)

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MTGO.description, domain=None, range=Optional[str])

slots.intersection = Slot(uri=MTGO.intersection, name="intersection", curie=MTGO.curie('intersection'),
                   model_uri=MTGO.intersection, domain=None, range=Optional[Union[str, NamedThingId]])

slots.union = Slot(uri=MTGO.union, name="union", curie=MTGO.curie('union'),
                   model_uri=MTGO.union, domain=None, range=Optional[Union[str, NamedThingId]])

slots.mana_cost = Slot(uri=MTGO.mana_cost, name="mana_cost", curie=MTGO.curie('mana_cost'),
                   model_uri=MTGO.mana_cost, domain=None, range=Optional[Union[Union[str, ManaCostId], List[Union[str, ManaCostId]]]])

slots.card_set = Slot(uri=MTGO.card_set, name="card_set", curie=MTGO.curie('card_set'),
                   model_uri=MTGO.card_set, domain=None, range=Optional[str])

slots.converted_mana_cost = Slot(uri=MTGO.converted_mana_cost, name="converted_mana_cost", curie=MTGO.curie('converted_mana_cost'),
                   model_uri=MTGO.converted_mana_cost, domain=None, range=Optional[int])

slots.ability = Slot(uri=MTGO.ability, name="ability", curie=MTGO.curie('ability'),
                   model_uri=MTGO.ability, domain=None, range=Optional[Union[Union[str, AbilityId], List[Union[str, AbilityId]]]])

slots.color = Slot(uri=MTGO.color, name="color", curie=MTGO.curie('color'),
                   model_uri=MTGO.color, domain=None, range=Union[Union[str, "Color"], List[Union[str, "Color"]]])

slots.rarity = Slot(uri=MTGO.rarity, name="rarity", curie=MTGO.curie('rarity'),
                   model_uri=MTGO.rarity, domain=None, range=Optional[Union[str, "Rarity"]])

slots.artist = Slot(uri=MTGO.artist, name="artist", curie=MTGO.curie('artist'),
                   model_uri=MTGO.artist, domain=None, range=Optional[str])

slots.flavor_text = Slot(uri=MTGO.flavor_text, name="flavor_text", curie=MTGO.curie('flavor_text'),
                   model_uri=MTGO.flavor_text, domain=None, range=Optional[str])

slots.oracle_text = Slot(uri=MTGO.oracle_text, name="oracle_text", curie=MTGO.curie('oracle_text'),
                   model_uri=MTGO.oracle_text, domain=None, range=Optional[str])

slots.power = Slot(uri=MTGO.power, name="power", curie=MTGO.curie('power'),
                   model_uri=MTGO.power, domain=None, range=int)

slots.toughness = Slot(uri=MTGO.toughness, name="toughness", curie=MTGO.curie('toughness'),
                   model_uri=MTGO.toughness, domain=None, range=int)

slots.variable_power = Slot(uri=MTGO.variable_power, name="variable_power", curie=MTGO.curie('variable_power'),
                   model_uri=MTGO.variable_power, domain=None, range=Optional[Union[bool, Bool]])

slots.variable_toughness = Slot(uri=MTGO.variable_toughness, name="variable_toughness", curie=MTGO.curie('variable_toughness'),
                   model_uri=MTGO.variable_toughness, domain=None, range=Optional[Union[bool, Bool]])

slots.variable_cost = Slot(uri=MTGO.variable_cost, name="variable_cost", curie=MTGO.curie('variable_cost'),
                   model_uri=MTGO.variable_cost, domain=None, range=Optional[Union[bool, Bool]])

slots.hybrid = Slot(uri=MTGO.hybrid, name="hybrid", curie=MTGO.curie('hybrid'),
                   model_uri=MTGO.hybrid, domain=None, range=Optional[Union[bool, Bool]])

slots.phyrexian = Slot(uri=MTGO.phyrexian, name="phyrexian", curie=MTGO.curie('phyrexian'),
                   model_uri=MTGO.phyrexian, domain=None, range=Optional[Union[bool, Bool]])

slots.snow = Slot(uri=MTGO.snow, name="snow", curie=MTGO.curie('snow'),
                   model_uri=MTGO.snow, domain=None, range=Optional[Union[bool, Bool]])

slots.type_line = Slot(uri=MTGO.type_line, name="type_line", curie=MTGO.curie('type_line'),
                   model_uri=MTGO.type_line, domain=None, range=str)

slots.card_subtype = Slot(uri=MTGO.card_subtype, name="card_subtype", curie=MTGO.curie('card_subtype'),
                   model_uri=MTGO.card_subtype, domain=None, range=Optional[Union[str, List[str]]])

slots.card_supertype = Slot(uri=MTGO.card_supertype, name="card_supertype", curie=MTGO.curie('card_supertype'),
                   model_uri=MTGO.card_supertype, domain=None, range=Optional[Union[str, List[str]]])

slots.card_type = Slot(uri=MTGO.card_type, name="card_type", curie=MTGO.curie('card_type'),
                   model_uri=MTGO.card_type, domain=None, range=str)

slots.value = Slot(uri=MTGO.value, name="value", curie=MTGO.curie('value'),
                   model_uri=MTGO.value, domain=None, range=Optional[int])

slots.rules_text = Slot(uri=MTGO.rules_text, name="rules_text", curie=MTGO.curie('rules_text'),
                   model_uri=MTGO.rules_text, domain=None, range=Optional[str])

slots.cost = Slot(uri=MTGO.cost, name="cost", curie=MTGO.curie('cost'),
                   model_uri=MTGO.cost, domain=None, range=Optional[Union[str, List[str]]])

slots.effect = Slot(uri=MTGO.effect, name="effect", curie=MTGO.curie('effect'),
                   model_uri=MTGO.effect, domain=None, range=Optional[Union[str, ConditionId]])

slots.action = Slot(uri=MTGO.action, name="action", curie=MTGO.curie('action'),
                   model_uri=MTGO.action, domain=None, range=Union[str, "Action"])

slots.source = Slot(uri=MTGO.source, name="source", curie=MTGO.curie('source'),
                   model_uri=MTGO.source, domain=None, range=Optional[str])

slots.target = Slot(uri=MTGO.target, name="target", curie=MTGO.curie('target'),
                   model_uri=MTGO.target, domain=None, range=Optional[str])

slots.condition = Slot(uri=MTGO.condition, name="condition", curie=MTGO.curie('condition'),
                   model_uri=MTGO.condition, domain=None, range=Optional[Union[str, ConditionId]])

slots.value_spec = Slot(uri=MTGO.value_spec, name="value_spec", curie=MTGO.curie('value_spec'),
                   model_uri=MTGO.value_spec, domain=None, range=Optional[Union[Union[str, ValueSpecificationId], List[Union[str, ValueSpecificationId]]]])

slots.time_spec = Slot(uri=MTGO.time_spec, name="time_spec", curie=MTGO.curie('time_spec'),
                   model_uri=MTGO.time_spec, domain=None, range=Optional[Union[Union[str, TimeSpecificationId], List[Union[str, TimeSpecificationId]]]])

slots.action_spec = Slot(uri=MTGO.action_spec, name="action_spec", curie=MTGO.curie('action_spec'),
                   model_uri=MTGO.action_spec, domain=None, range=Optional[Union[Union[str, ActionSpecificationId], List[Union[str, ActionSpecificationId]]]])

slots.player = Slot(uri=MTGO.player, name="player", curie=MTGO.curie('player'),
                   model_uri=MTGO.player, domain=None, range=Optional[Union[str, "Player"]])

slots.turn_phase = Slot(uri=MTGO.turn_phase, name="turn_phase", curie=MTGO.curie('turn_phase'),
                   model_uri=MTGO.turn_phase, domain=None, range=Optional[Union[str, "TurnPhase"]])

slots.unit = Slot(uri=MTGO.unit, name="unit", curie=MTGO.curie('unit'),
                   model_uri=MTGO.unit, domain=None, range=Optional[str])

slots.constraint = Slot(uri=MTGO.constraint, name="constraint", curie=MTGO.curie('constraint'),
                   model_uri=MTGO.constraint, domain=None, range=Optional[str])

slots.ability_keyword = Slot(uri=MTGO.ability_keyword, name="ability_keyword", curie=MTGO.curie('ability_keyword'),
                   model_uri=MTGO.ability_keyword, domain=None, range=Optional[str])

slots.power_modifier = Slot(uri=MTGO.power_modifier, name="power_modifier", curie=MTGO.curie('power_modifier'),
                   model_uri=MTGO.power_modifier, domain=None, range=Optional[int])

slots.toughness_modifier = Slot(uri=MTGO.toughness_modifier, name="toughness_modifier", curie=MTGO.curie('toughness_modifier'),
                   model_uri=MTGO.toughness_modifier, domain=None, range=Optional[int])

slots.cardCollection__cards = Slot(uri=MTGO.cards, name="cardCollection__cards", curie=MTGO.curie('cards'),
                   model_uri=MTGO.cardCollection__cards, domain=None, range=Optional[Union[Dict[Union[str, CardId], Union[dict, Card]], List[Union[dict, Card]]]])

slots.cardCollection__costs = Slot(uri=MTGO.costs, name="cardCollection__costs", curie=MTGO.curie('costs'),
                   model_uri=MTGO.cardCollection__costs, domain=None, range=Optional[Union[Dict[Union[str, CostId], Union[dict, Cost]], List[Union[dict, Cost]]]])

slots.abilityCollection__activated_abilities = Slot(uri=MTGO.activated_abilities, name="abilityCollection__activated_abilities", curie=MTGO.curie('activated_abilities'),
                   model_uri=MTGO.abilityCollection__activated_abilities, domain=None, range=Optional[Union[Dict[Union[str, ActivatedAbilityId], Union[dict, ActivatedAbility]], List[Union[dict, ActivatedAbility]]]])

slots.abilityCollection__conditions = Slot(uri=MTGO.conditions, name="abilityCollection__conditions", curie=MTGO.curie('conditions'),
                   model_uri=MTGO.abilityCollection__conditions, domain=None, range=Optional[Union[Dict[Union[str, ConditionId], Union[dict, Condition]], List[Union[dict, Condition]]]])

slots.abilityCollection__mana_costs = Slot(uri=MTGO.mana_costs, name="abilityCollection__mana_costs", curie=MTGO.curie('mana_costs'),
                   model_uri=MTGO.abilityCollection__mana_costs, domain=None, range=Optional[Union[Dict[Union[str, ManaCostId], Union[dict, ManaCost]], List[Union[dict, ManaCost]]]])

slots.abilityCollection__value_specifications = Slot(uri=MTGO.value_specifications, name="abilityCollection__value_specifications", curie=MTGO.curie('value_specifications'),
                   model_uri=MTGO.abilityCollection__value_specifications, domain=None, range=Optional[Union[Dict[Union[str, ValueSpecificationId], Union[dict, ValueSpecification]], List[Union[dict, ValueSpecification]]]])

slots.abilityCollection__action_specifications = Slot(uri=MTGO.action_specifications, name="abilityCollection__action_specifications", curie=MTGO.curie('action_specifications'),
                   model_uri=MTGO.abilityCollection__action_specifications, domain=None, range=Optional[Union[Dict[Union[str, ActionSpecificationId], Union[dict, ActionSpecification]], List[Union[dict, ActionSpecification]]]])

slots.abilityCollection__time_specifications = Slot(uri=MTGO.time_specifications, name="abilityCollection__time_specifications", curie=MTGO.curie('time_specifications'),
                   model_uri=MTGO.abilityCollection__time_specifications, domain=None, range=Optional[Union[Dict[Union[str, TimeSpecificationId], Union[dict, TimeSpecification]], List[Union[dict, TimeSpecification]]]])

slots.Cost_intersection = Slot(uri=MTGO.intersection, name="Cost_intersection", curie=MTGO.curie('intersection'),
                   model_uri=MTGO.Cost_intersection, domain=Cost, range=Optional[Union[str, CostId]])

slots.Cost_union = Slot(uri=MTGO.union, name="Cost_union", curie=MTGO.curie('union'),
                   model_uri=MTGO.Cost_union, domain=Cost, range=Optional[Union[str, CostId]])

slots.ActionSpecification_intersection = Slot(uri=MTGO.intersection, name="ActionSpecification_intersection", curie=MTGO.curie('intersection'),
                   model_uri=MTGO.ActionSpecification_intersection, domain=ActionSpecification, range=Optional[Union[str, ActionSpecificationId]])

slots.ActionSpecification_union = Slot(uri=MTGO.union, name="ActionSpecification_union", curie=MTGO.curie('union'),
                   model_uri=MTGO.ActionSpecification_union, domain=ActionSpecification, range=Optional[Union[str, ActionSpecificationId]])

slots.ActionSpecification_constraint = Slot(uri=MTGO.constraint, name="ActionSpecification_constraint", curie=MTGO.curie('constraint'),
                   model_uri=MTGO.ActionSpecification_constraint, domain=ActionSpecification, range=Optional[Union[str, "ActionConstraint"]])

slots.ValueSpecification_intersection = Slot(uri=MTGO.intersection, name="ValueSpecification_intersection", curie=MTGO.curie('intersection'),
                   model_uri=MTGO.ValueSpecification_intersection, domain=ValueSpecification, range=Optional[Union[str, ValueSpecificationId]])

slots.ValueSpecification_union = Slot(uri=MTGO.union, name="ValueSpecification_union", curie=MTGO.curie('union'),
                   model_uri=MTGO.ValueSpecification_union, domain=ValueSpecification, range=Optional[Union[str, ValueSpecificationId]])

slots.ValueSpecification_constraint = Slot(uri=MTGO.constraint, name="ValueSpecification_constraint", curie=MTGO.curie('constraint'),
                   model_uri=MTGO.ValueSpecification_constraint, domain=ValueSpecification, range=Optional[Union[str, "ValueConstraint"]])

slots.TimeSpecification_intersection = Slot(uri=MTGO.intersection, name="TimeSpecification_intersection", curie=MTGO.curie('intersection'),
                   model_uri=MTGO.TimeSpecification_intersection, domain=TimeSpecification, range=Optional[Union[str, TimeSpecificationId]])

slots.TimeSpecification_union = Slot(uri=MTGO.union, name="TimeSpecification_union", curie=MTGO.curie('union'),
                   model_uri=MTGO.TimeSpecification_union, domain=TimeSpecification, range=Optional[Union[str, TimeSpecificationId]])

slots.TimeSpecification_constraint = Slot(uri=MTGO.constraint, name="TimeSpecification_constraint", curie=MTGO.curie('constraint'),
                   model_uri=MTGO.TimeSpecification_constraint, domain=TimeSpecification, range=Optional[Union[str, "TimeConstraint"]])