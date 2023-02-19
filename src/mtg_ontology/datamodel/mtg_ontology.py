# Auto generated from mtg_ontology.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-19T19:01:06
# Schema: mtg-ontology
#
# id: https://w3id.org/cmdoret/mtg-ontology
# description: An ontology describing Magic: The Gathering.
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
from linkml_runtime.linkml_model.types import Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EXAMPLE = CurieNamespace('example', 'http://www.example.org/rdf#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MTGO = CurieNamespace('mtgo', 'https://w3id.org/cmdoret/mtg-ontology/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
WIKI = CurieNamespace('wiki', 'http://en.wikipedia.org/wiki/')
DEFAULT_ = MTGO


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class CardId(NamedThingId):
    pass


class SpellId(NamedThingId):
    pass


class PermanentId(CardId):
    pass


class TokenId(CardId):
    pass


class SorceryId(CardId):
    pass


class InstantId(CardId):
    pass


class EnchantmentId(PermanentId):
    pass


class ArtifactId(PermanentId):
    pass


class CreatureId(PermanentId):
    pass


class LandId(PermanentId):
    pass


class CostId(NamedThingId):
    pass


class ManaCostId(CostId):
    pass


class LifeCostId(CostId):
    pass


class AbilityId(NamedThingId):
    pass


class ActivatedAbilityId(AbilityId):
    pass


class KeywordAbilityId(AbilityId):
    pass


class StaticAbilityId(AbilityId):
    pass


class TriggeredAbilityId(AbilityId):
    pass


class EventId(NamedThingId):
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
    ability: Optional[Union[Union[str, AbilityId], List[Union[str, AbilityId]]]] = empty_list()
    additional_cost: Optional[str] = None
    mana_cost: Optional[Union[Union[str, ManaCostId], List[Union[str, ManaCostId]]]] = empty_list()
    converted_mana_cost: Optional[int] = None
    card_set: Optional[str] = None
    artist: Optional[str] = None
    flavor_text: Optional[str] = None
    card_subtype: Optional[Union[str, List[str]]] = empty_list()
    card_supertype: Optional[Union[str, List[str]]] = empty_list()
    rarity: Optional[Union[str, "Rarity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CardId):
            self.id = CardId(self.id)

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

        if not isinstance(self.ability, list):
            self.ability = [self.ability] if self.ability is not None else []
        self.ability = [v if isinstance(v, AbilityId) else AbilityId(v) for v in self.ability]

        if self.additional_cost is not None and not isinstance(self.additional_cost, str):
            self.additional_cost = str(self.additional_cost)

        if not isinstance(self.mana_cost, list):
            self.mana_cost = [self.mana_cost] if self.mana_cost is not None else []
        self.mana_cost = [v if isinstance(v, ManaCostId) else ManaCostId(v) for v in self.mana_cost]

        if self.converted_mana_cost is not None and not isinstance(self.converted_mana_cost, int):
            self.converted_mana_cost = int(self.converted_mana_cost)

        if self.card_set is not None and not isinstance(self.card_set, str):
            self.card_set = str(self.card_set)

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

        super().__post_init__(**kwargs)


@dataclass
class Spell(NamedThing):
    """
    An object on the stack. Either a card that has been cast, or a copy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Spell
    class_class_curie: ClassVar[str] = "mtgo:Spell"
    class_name: ClassVar[str] = "Spell"
    class_model_uri: ClassVar[URIRef] = MTGO.Spell

    id: Union[str, SpellId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpellId):
            self.id = SpellId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Permanent(Card):
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
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    type_line: str = None
    card_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PermanentId):
            self.id = PermanentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Token(Card):
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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TokenId):
            self.id = TokenId(self.id)

        super().__post_init__(**kwargs)


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
class Enchantment(Permanent):
    """
    A permanent which applies persistent magical effects.
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
class Artifact(Permanent):
    """
    A permanent representing a magical item, animated construct, or other objects and devices.
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
class Creature(Permanent):
    """
    A card that represents a creature that can be summoned to the battlefield.
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

        super().__post_init__(**kwargs)


@dataclass
class Land(Permanent):
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
class Cost(NamedThing):
    """
    The cost of a card or ability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Cost
    class_class_curie: ClassVar[str] = "mtgo:Cost"
    class_name: ClassVar[str] = "Cost"
    class_model_uri: ClassVar[URIRef] = MTGO.Cost

    id: Union[str, CostId] = None
    name: str = None
    value: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CostId):
            self.id = CostId(self.id)

        if self.value is not None and not isinstance(self.value, int):
            self.value = int(self.value)

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
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None

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
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LifeCostId):
            self.id = LifeCostId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Ability(NamedThing):
    """
    A card ability, activated, triggered or static.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Ability
    class_class_curie: ClassVar[str] = "mtgo:Ability"
    class_name: ClassVar[str] = "Ability"
    class_model_uri: ClassVar[URIRef] = MTGO.Ability

    id: Union[str, AbilityId] = None
    name: str = None
    rules_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AbilityId):
            self.id = AbilityId(self.id)

        if self.rules_text is not None and not isinstance(self.rules_text, str):
            self.rules_text = str(self.rules_text)

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
    name: str = None
    additional_cost: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivatedAbilityId):
            self.id = ActivatedAbilityId(self.id)

        if self.additional_cost is not None and not isinstance(self.additional_cost, str):
            self.additional_cost = str(self.additional_cost)

        super().__post_init__(**kwargs)


@dataclass
class KeywordAbility(Ability):
    """
    A passive ability represented by word that substitutes for a piece of rules text, such as deathtouch or flying.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.KeywordAbility
    class_class_curie: ClassVar[str] = "mtgo:KeywordAbility"
    class_name: ClassVar[str] = "KeywordAbility"
    class_model_uri: ClassVar[URIRef] = MTGO.KeywordAbility

    id: Union[str, KeywordAbilityId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeywordAbilityId):
            self.id = KeywordAbilityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

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
    name: str = None

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
    name: str = None
    condition: Optional[Union[str, EventId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TriggeredAbilityId):
            self.id = TriggeredAbilityId(self.id)

        if self.condition is not None and not isinstance(self.condition, EventId):
            self.condition = EventId(self.condition)

        super().__post_init__(**kwargs)


@dataclass
class Event(NamedThing):
    """
    A combination of circumstances during a game.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.Event
    class_class_curie: ClassVar[str] = "mtgo:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = MTGO.Event

    id: Union[str, EventId] = None
    name: str = None
    action: Union[str, "Action"] = None
    source: Optional[str] = None
    target: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, Action):
            self.action = Action(self.action)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.target is not None and not isinstance(self.target, str):
            self.target = str(self.target)

        super().__post_init__(**kwargs)


@dataclass
class CardCollection(YAMLRoot):
    """
    A collection of Cards, such as a Deck or cards set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGO.CardCollection
    class_class_curie: ClassVar[str] = "mtgo:CardCollection"
    class_name: ClassVar[str] = "CardCollection"
    class_model_uri: ClassVar[URIRef] = MTGO.CardCollection

    entries: Optional[Union[Dict[Union[str, CardId], Union[dict, Card]], List[Union[dict, Card]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Card, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class Color(EnumDefinitionImpl):
    """
    A color, such as Black, Blue, Red, Green, White or Colorless.
    """
    black = PermissibleValue(text="black",
                                 description="The color black, associated with darkness.",
                                 meaning=WIKI.Q23445)
    blue = PermissibleValue(text="blue",
                               description="The color blue, associated with water.",
                               meaning=WIKI.Q1088)
    green = PermissibleValue(text="green",
                                 description="The color green, associated with nature.",
                                 meaning=WIKI.Q3133)
    red = PermissibleValue(text="red",
                             description="The color red, associated with fire.",
                             meaning=WIKI.Q3142)
    white = PermissibleValue(text="white",
                                 description="The color white, associated with light.",
                                 meaning=WIKI.Q23444)
    colorless = PermissibleValue(text="colorless",
                                         description="Absence of color.",
                                         meaning=WIKI.Q1396399)

    _defn = EnumDefinition(
        name="Color",
        description="A color, such as Black, Blue, Red, Green, White or Colorless.",
    )

class Rarity(EnumDefinitionImpl):
    """
    The rarity of the card, may be one of Common, Uncommon, Rare or Mythic.
    """
    common = PermissibleValue(text="common",
                                   description="The lowest rarity level, identified by a black set image.")
    uncommon = PermissibleValue(text="uncommon",
                                       description="The second lowest rarity level, identified by a silver set image.")
    rare = PermissibleValue(text="rare",
                               description="The second highest rarity level, identified by a golden set image.")
    mythic = PermissibleValue(text="mythic",
                                   description="The highest rarity level, identified by a red set image.")

    _defn = EnumDefinition(
        name="Rarity",
        description="The rarity of the card, may be one of Common, Uncommon, Rare or Mythic.",
    )

class Player(EnumDefinitionImpl):
    """
    One or more human players.
    """
    you = PermissibleValue(text="you",
                             description="The focal human player.")
    owner = PermissibleValue(text="owner",
                                 description="The human player who owns a card.")
    controller = PermissibleValue(text="controller",
                                           description="The human player who controls an object on the stack.")
    opponent = PermissibleValue(text="opponent",
                                       description="A human player playing against the focal player.")
    opponents = PermissibleValue(text="opponents",
                                         description="All human players playing against the focal player.")
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
    discard = PermissibleValue(text="discard",
                                     description="Transfer one or more cards from the hand to the graveyard.")
    draw = PermissibleValue(text="draw",
                               description="Transfer one or more cards from the library to the hand.")
    sacrifice = PermissibleValue(text="sacrifice",
                                         description="Transfer one or more cards from the battlefield to the graveyard.")
    exile = PermissibleValue(text="exile",
                                 description="Remove one or more cards from game.")
    fight = PermissibleValue(text="fight",
                                 description="Two cards fight each other.")
    deal_damage = PermissibleValue(text="deal_damage",
                                             description="Something deals damage to something else.")

    _defn = EnumDefinition(
        name="Action",
        description="An action taken by a player or card.",
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

slots.additional_cost = Slot(uri=MTGO.additional_cost, name="additional_cost", curie=MTGO.curie('additional_cost'),
                   model_uri=MTGO.additional_cost, domain=None, range=Optional[str])

slots.mana_cost = Slot(uri=MTGO.mana_cost, name="mana_cost", curie=MTGO.curie('mana_cost'),
                   model_uri=MTGO.mana_cost, domain=None, range=Optional[Union[Union[str, ManaCostId], List[Union[str, ManaCostId]]]])

slots.card_set = Slot(uri=MTGO.card_set, name="card_set", curie=MTGO.curie('card_set'),
                   model_uri=MTGO.card_set, domain=None, range=Optional[str])

slots.converted_mana_cost = Slot(uri=MTGO.converted_mana_cost, name="converted_mana_cost", curie=MTGO.curie('converted_mana_cost'),
                   model_uri=MTGO.converted_mana_cost, domain=None, range=Optional[int])

slots.color = Slot(uri=MTGO.color, name="color", curie=MTGO.curie('color'),
                   model_uri=MTGO.color, domain=None, range=Union[Union[str, "Color"], List[Union[str, "Color"]]])

slots.ability = Slot(uri=MTGO.ability, name="ability", curie=MTGO.curie('ability'),
                   model_uri=MTGO.ability, domain=None, range=Optional[Union[Union[str, AbilityId], List[Union[str, AbilityId]]]])

slots.rarity = Slot(uri=MTGO.rarity, name="rarity", curie=MTGO.curie('rarity'),
                   model_uri=MTGO.rarity, domain=None, range=Optional[Union[str, "Rarity"]])

slots.artist = Slot(uri=MTGO.artist, name="artist", curie=MTGO.curie('artist'),
                   model_uri=MTGO.artist, domain=None, range=Optional[str])

slots.flavor_text = Slot(uri=MTGO.flavor_text, name="flavor_text", curie=MTGO.curie('flavor_text'),
                   model_uri=MTGO.flavor_text, domain=None, range=Optional[str])

slots.rules_text = Slot(uri=MTGO.rules_text, name="rules_text", curie=MTGO.curie('rules_text'),
                   model_uri=MTGO.rules_text, domain=None, range=Optional[str])

slots.power = Slot(uri=MTGO.power, name="power", curie=MTGO.curie('power'),
                   model_uri=MTGO.power, domain=None, range=int)

slots.toughness = Slot(uri=MTGO.toughness, name="toughness", curie=MTGO.curie('toughness'),
                   model_uri=MTGO.toughness, domain=None, range=int)

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

slots.action = Slot(uri=MTGO.action, name="action", curie=MTGO.curie('action'),
                   model_uri=MTGO.action, domain=None, range=Union[str, "Action"])

slots.source = Slot(uri=MTGO.source, name="source", curie=MTGO.curie('source'),
                   model_uri=MTGO.source, domain=None, range=Optional[str])

slots.target = Slot(uri=MTGO.target, name="target", curie=MTGO.curie('target'),
                   model_uri=MTGO.target, domain=None, range=Optional[str])

slots.condition = Slot(uri=MTGO.condition, name="condition", curie=MTGO.curie('condition'),
                   model_uri=MTGO.condition, domain=None, range=Optional[Union[str, EventId]])

slots.cardCollection__entries = Slot(uri=MTGO.entries, name="cardCollection__entries", curie=MTGO.curie('entries'),
                   model_uri=MTGO.cardCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, CardId], Union[dict, Card]], List[Union[dict, Card]]]])