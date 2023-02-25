# Auto generated from mtg_ontology.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-25T03:32:57
# Schema: mtgo
#
# id: https://w3id.org/cmdoret/mtg-ontology/
# description: An ontology describing Magic: The Gathering. It provides the basic features needed to describe
#              cards.
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
MTGO = CurieNamespace('mtgo', 'https://w3id.org/cmdoret/mtg-ontology/')
MTGOA = CurieNamespace('mtgoa', 'https://w3id.org/cmdoret/mtg-ontology/abilities/')
MTGOC = CurieNamespace('mtgoc', 'https://w3id.org/cmdoret/mtg-ontology/cards/')
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


class ManaId(NamedThingId):
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


class ConditionId(NamedThingId):
    pass


class SpecificationId(NamedThingId):
    pass


class ActionSpecificationId(SpecificationId):
    pass


class ValueSpecificationId(SpecificationId):
    pass


class TimeSpecificationId(NamedThingId):
    pass


class PropertyId(NamedThingId):
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Card
    class_class_curie: ClassVar[str] = "mtgoc:Card"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Spell
    class_class_curie: ClassVar[str] = "mtgoc:Spell"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Permanent
    class_class_curie: ClassVar[str] = "mtgoc:Permanent"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Token
    class_class_curie: ClassVar[str] = "mtgoc:Token"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Sorcery
    class_class_curie: ClassVar[str] = "mtgoc:Sorcery"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Instant
    class_class_curie: ClassVar[str] = "mtgoc:Instant"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Enchantment
    class_class_curie: ClassVar[str] = "mtgoc:Enchantment"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Artifact
    class_class_curie: ClassVar[str] = "mtgoc:Artifact"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Creature
    class_class_curie: ClassVar[str] = "mtgoc:Creature"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Land
    class_class_curie: ClassVar[str] = "mtgoc:Land"
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

    class_class_uri: ClassVar[URIRef] = MTGOC.Cost
    class_class_curie: ClassVar[str] = "mtgoc:Cost"
    class_name: ClassVar[str] = "Cost"
    class_model_uri: ClassVar[URIRef] = MTGO.Cost

    id: Union[str, CostId] = None
    name: str = None
    value: Optional[int] = None
    and: Optional[Union[str, CostId]] = None
    or: Optional[Union[str, CostId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CostId):
            self.id = CostId(self.id)

        if self.value is not None and not isinstance(self.value, int):
            self.value = int(self.value)

        if self.and is not None and not isinstance(self.and, CostId):
            self.and = CostId(self.and)

        if self.or is not None and not isinstance(self.or, CostId):
            self.or = CostId(self.or)

        super().__post_init__(**kwargs)


@dataclass
class ManaCost(Cost):
    """
    The mana cost of a card or ability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOC.ManaCost
    class_class_curie: ClassVar[str] = "mtgoc:ManaCost"
    class_name: ClassVar[str] = "ManaCost"
    class_model_uri: ClassVar[URIRef] = MTGO.ManaCost

    id: Union[str, ManaCostId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    snow: Optional[Union[bool, Bool]] = None

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

        super().__post_init__(**kwargs)


@dataclass
class LifeCost(Cost):
    """
    The life cost of a card or ability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOC.LifeCost
    class_class_curie: ClassVar[str] = "mtgoc:LifeCost"
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
class Mana(NamedThing):
    """
    A mana in the pool.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOC.Mana
    class_class_curie: ClassVar[str] = "mtgoc:Mana"
    class_name: ClassVar[str] = "Mana"
    class_model_uri: ClassVar[URIRef] = MTGO.Mana

    id: Union[str, ManaId] = None
    name: str = None
    color: Union[Union[str, "Color"], List[Union[str, "Color"]]] = None
    snow: Optional[Union[bool, Bool]] = None

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

        super().__post_init__(**kwargs)


@dataclass
class CardCollection(YAMLRoot):
    """
    A collection of Cards, such as a Deck or cards set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOC.CardCollection
    class_class_curie: ClassVar[str] = "mtgoc:CardCollection"
    class_name: ClassVar[str] = "CardCollection"
    class_model_uri: ClassVar[URIRef] = MTGO.CardCollection

    entries: Optional[Union[Dict[Union[str, CardId], Union[dict, Card]], List[Union[dict, Card]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Card, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Ability(NamedThing):
    """
    A card ability, activated, triggered or static.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.Ability
    class_class_curie: ClassVar[str] = "mtgoa:Ability"
    class_name: ClassVar[str] = "Ability"
    class_model_uri: ClassVar[URIRef] = MTGO.Ability

    id: Union[str, AbilityId] = None
    name: str = None
    rules_text: Optional[str] = None
    effect: Optional[Union[str, ConditionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AbilityId):
            self.id = AbilityId(self.id)

        if self.rules_text is not None and not isinstance(self.rules_text, str):
            self.rules_text = str(self.rules_text)

        if self.effect is not None and not isinstance(self.effect, ConditionId):
            self.effect = ConditionId(self.effect)

        super().__post_init__(**kwargs)


@dataclass
class ActivatedAbility(Ability):
    """
    A card ability which can be activated for a cost.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.ActivatedAbility
    class_class_curie: ClassVar[str] = "mtgoa:ActivatedAbility"
    class_name: ClassVar[str] = "ActivatedAbility"
    class_model_uri: ClassVar[URIRef] = MTGO.ActivatedAbility

    id: Union[str, ActivatedAbilityId] = None
    name: str = None
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
class KeywordAbility(Ability):
    """
    A passive ability represented by word that substitutes for a piece of rules text, such as deathtouch or flying.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.KeywordAbility
    class_class_curie: ClassVar[str] = "mtgoa:KeywordAbility"
    class_name: ClassVar[str] = "KeywordAbility"
    class_model_uri: ClassVar[URIRef] = MTGO.KeywordAbility

    id: Union[str, KeywordAbilityId] = None
    name: str = None
    value: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeywordAbilityId):
            self.id = KeywordAbilityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass
class StaticAbility(Ability):
    """
    A card ability which remains active until endgame once put into effect.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.StaticAbility
    class_class_curie: ClassVar[str] = "mtgoa:StaticAbility"
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

    class_class_uri: ClassVar[URIRef] = MTGOA.TriggeredAbility
    class_class_curie: ClassVar[str] = "mtgoa:TriggeredAbility"
    class_name: ClassVar[str] = "TriggeredAbility"
    class_model_uri: ClassVar[URIRef] = MTGO.TriggeredAbility

    id: Union[str, TriggeredAbilityId] = None
    name: str = None
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
class Condition(NamedThing):
    """
    A condition expressed as constraints.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.Condition
    class_class_curie: ClassVar[str] = "mtgoa:Condition"
    class_name: ClassVar[str] = "Condition"
    class_model_uri: ClassVar[URIRef] = MTGO.Condition

    id: Union[str, ConditionId] = None
    name: str = None
    source: Optional[str] = None
    target: Optional[str] = None
    property: Optional[Union[str, PropertyId]] = None
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

        if self.property is not None and not isinstance(self.property, PropertyId):
            self.property = PropertyId(self.property)

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
class Specification(NamedThing):
    """
    A specification for a thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.Specification
    class_class_curie: ClassVar[str] = "mtgoa:Specification"
    class_name: ClassVar[str] = "Specification"
    class_model_uri: ClassVar[URIRef] = MTGO.Specification

    id: Union[str, SpecificationId] = None
    name: str = None
    constraint: Optional[str] = None
    and: Optional[Union[str, NamedThingId]] = None
    or: Optional[Union[str, NamedThingId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecificationId):
            self.id = SpecificationId(self.id)

        if self.constraint is not None and not isinstance(self.constraint, str):
            self.constraint = str(self.constraint)

        if self.and is not None and not isinstance(self.and, NamedThingId):
            self.and = NamedThingId(self.and)

        if self.or is not None and not isinstance(self.or, NamedThingId):
            self.or = NamedThingId(self.or)

        super().__post_init__(**kwargs)


@dataclass
class ActionSpecification(Specification):
    """
    A specification for an action.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.ActionSpecification
    class_class_curie: ClassVar[str] = "mtgoa:ActionSpecification"
    class_name: ClassVar[str] = "ActionSpecification"
    class_model_uri: ClassVar[URIRef] = MTGO.ActionSpecification

    id: Union[str, ActionSpecificationId] = None
    name: str = None
    action: Union[str, "Action"] = None
    and: Optional[Union[str, ActionSpecificationId]] = None
    or: Optional[Union[str, ActionSpecificationId]] = None
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

        if self.and is not None and not isinstance(self.and, ActionSpecificationId):
            self.and = ActionSpecificationId(self.and)

        if self.or is not None and not isinstance(self.or, ActionSpecificationId):
            self.or = ActionSpecificationId(self.or)

        if self.constraint is not None and not isinstance(self.constraint, ActionConstraint):
            self.constraint = ActionConstraint(self.constraint)

        super().__post_init__(**kwargs)


@dataclass
class ValueSpecification(Specification):
    """
    A specification for a quantitative value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.ValueSpecification
    class_class_curie: ClassVar[str] = "mtgoa:ValueSpecification"
    class_name: ClassVar[str] = "ValueSpecification"
    class_model_uri: ClassVar[URIRef] = MTGO.ValueSpecification

    id: Union[str, ValueSpecificationId] = None
    name: str = None
    value: Optional[int] = None
    unit: Optional[str] = None
    and: Optional[Union[str, ValueSpecificationId]] = None
    or: Optional[Union[str, ValueSpecificationId]] = None
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

        if self.and is not None and not isinstance(self.and, ValueSpecificationId):
            self.and = ValueSpecificationId(self.and)

        if self.or is not None and not isinstance(self.or, ValueSpecificationId):
            self.or = ValueSpecificationId(self.or)

        if self.constraint is not None and not isinstance(self.constraint, ValueConstraint):
            self.constraint = ValueConstraint(self.constraint)

        super().__post_init__(**kwargs)


@dataclass
class TimeSpecification(NamedThing):
    """
    A specification for a time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.TimeSpecification
    class_class_curie: ClassVar[str] = "mtgoa:TimeSpecification"
    class_name: ClassVar[str] = "TimeSpecification"
    class_model_uri: ClassVar[URIRef] = MTGO.TimeSpecification

    id: Union[str, TimeSpecificationId] = None
    name: str = None
    time: Optional[Union[str, "Time"]] = None
    player: Optional[Union[str, "Player"]] = None
    and: Optional[Union[str, TimeSpecificationId]] = None
    or: Optional[Union[str, TimeSpecificationId]] = None
    constraint: Optional[Union[str, "TimeConstraint"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TimeSpecificationId):
            self.id = TimeSpecificationId(self.id)

        if self.time is not None and not isinstance(self.time, Time):
            self.time = Time(self.time)

        if self.player is not None and not isinstance(self.player, Player):
            self.player = Player(self.player)

        if self.and is not None and not isinstance(self.and, TimeSpecificationId):
            self.and = TimeSpecificationId(self.and)

        if self.or is not None and not isinstance(self.or, TimeSpecificationId):
            self.or = TimeSpecificationId(self.or)

        if self.constraint is not None and not isinstance(self.constraint, TimeConstraint):
            self.constraint = TimeConstraint(self.constraint)

        super().__post_init__(**kwargs)


@dataclass
class Property(NamedThing):
    """
    A property of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTGOA.Property
    class_class_curie: ClassVar[str] = "mtgoa:Property"
    class_name: ClassVar[str] = "Property"
    class_model_uri: ClassVar[URIRef] = MTGO.Property

    id: Union[str, PropertyId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PropertyId):
            self.id = PropertyId(self.id)

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
    cast = PermissibleValue(text="cast",
                               description="A spell is cast.")
    activate = PermissibleValue(text="activate",
                                       description="An ability is activated.")
    place_creature = PermissibleValue(text="place_creature",
                                                   description="One or more creatures are placed on the battlefield.")
    tap = PermissibleValue(text="tap",
                             description="A card is tapped.")
    untap = PermissibleValue(text="untap",
                                 description="A card is untapped")
    add_mana = PermissibleValue(text="add_mana",
                                       description="A player adds mana to their mana pool.")
    control = PermissibleValue(text="control",
                                     description="A player controls a card.")

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

class Time(EnumDefinitionImpl):
    """
    A time during the turn.
    """
    beginning_phase = PermissibleValue(text="beginning_phase",
                                                     description="The beginning of the turn.")
    untap_step = PermissibleValue(text="untap_step",
                                           description="The untap step.")
    upkeep_step = PermissibleValue(text="upkeep_step",
                                             description="The upkeep step.")
    draw_step = PermissibleValue(text="draw_step",
                                         description="The draw step.")
    main_phase = PermissibleValue(text="main_phase",
                                           description="Either main phase.")
    pre_combat_main_phase = PermissibleValue(text="pre_combat_main_phase",
                                                                 description="The first main phase.")
    post_combat_main_phase = PermissibleValue(text="post_combat_main_phase",
                                                                   description="The second main phase.")
    combat_phase = PermissibleValue(text="combat_phase",
                                               description="The combat phase.")
    beginning_of_combat_step = PermissibleValue(text="beginning_of_combat_step",
                                                                       description="The first step of the combat phase.")
    declare_attackers_step = PermissibleValue(text="declare_attackers_step",
                                                                   description="The declare attackers step.")
    declare_blockers_step = PermissibleValue(text="declare_blockers_step",
                                                                 description="The declare blockers step.")
    combat_damage_step = PermissibleValue(text="combat_damage_step",
                                                           description="The combat damage step.")
    end_of_combat_step = PermissibleValue(text="end_of_combat_step",
                                                           description="The end of combat step.")
    ending_phase = PermissibleValue(text="ending_phase",
                                               description="The end step.")
    cleanup_step = PermissibleValue(text="cleanup_step",
                                               description="The cleanup step.")
    turn = PermissibleValue(text="turn",
                               description="A player turn.")

    _defn = EnumDefinition(
        name="Time",
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

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MTGO.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MTGO.name, domain=None, range=str)

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MTGO.description, domain=None, range=Optional[str])

slots.and = Slot(uri=MTGO.and, name="and", curie=MTGO.curie('and'),
                   model_uri=MTGO.and, domain=None, range=Optional[Union[str, NamedThingId]])

slots.or = Slot(uri=MTGO.or, name="or", curie=MTGO.curie('or'),
                   model_uri=MTGO.or, domain=None, range=Optional[Union[str, NamedThingId]])

slots.mana_cost = Slot(uri=MTGOC.mana_cost, name="mana_cost", curie=MTGOC.curie('mana_cost'),
                   model_uri=MTGO.mana_cost, domain=None, range=Optional[Union[Union[str, ManaCostId], List[Union[str, ManaCostId]]]])

slots.card_set = Slot(uri=MTGOC.card_set, name="card_set", curie=MTGOC.curie('card_set'),
                   model_uri=MTGO.card_set, domain=None, range=Optional[str])

slots.converted_mana_cost = Slot(uri=MTGOC.converted_mana_cost, name="converted_mana_cost", curie=MTGOC.curie('converted_mana_cost'),
                   model_uri=MTGO.converted_mana_cost, domain=None, range=Optional[int])

slots.color = Slot(uri=MTGOC.color, name="color", curie=MTGOC.curie('color'),
                   model_uri=MTGO.color, domain=None, range=Union[Union[str, "Color"], List[Union[str, "Color"]]])

slots.rarity = Slot(uri=MTGOC.rarity, name="rarity", curie=MTGOC.curie('rarity'),
                   model_uri=MTGO.rarity, domain=None, range=Optional[Union[str, "Rarity"]])

slots.artist = Slot(uri=MTGOC.artist, name="artist", curie=MTGOC.curie('artist'),
                   model_uri=MTGO.artist, domain=None, range=Optional[str])

slots.flavor_text = Slot(uri=MTGOC.flavor_text, name="flavor_text", curie=MTGOC.curie('flavor_text'),
                   model_uri=MTGO.flavor_text, domain=None, range=Optional[str])

slots.power = Slot(uri=MTGOC.power, name="power", curie=MTGOC.curie('power'),
                   model_uri=MTGO.power, domain=None, range=int)

slots.toughness = Slot(uri=MTGOC.toughness, name="toughness", curie=MTGOC.curie('toughness'),
                   model_uri=MTGO.toughness, domain=None, range=int)

slots.snow = Slot(uri=MTGOC.snow, name="snow", curie=MTGOC.curie('snow'),
                   model_uri=MTGO.snow, domain=None, range=Optional[Union[bool, Bool]])

slots.type_line = Slot(uri=MTGOC.type_line, name="type_line", curie=MTGOC.curie('type_line'),
                   model_uri=MTGO.type_line, domain=None, range=str)

slots.card_subtype = Slot(uri=MTGOC.card_subtype, name="card_subtype", curie=MTGOC.curie('card_subtype'),
                   model_uri=MTGO.card_subtype, domain=None, range=Optional[Union[str, List[str]]])

slots.card_supertype = Slot(uri=MTGOC.card_supertype, name="card_supertype", curie=MTGOC.curie('card_supertype'),
                   model_uri=MTGO.card_supertype, domain=None, range=Optional[Union[str, List[str]]])

slots.card_type = Slot(uri=MTGOC.card_type, name="card_type", curie=MTGOC.curie('card_type'),
                   model_uri=MTGO.card_type, domain=None, range=str)

slots.value = Slot(uri=MTGOC.value, name="value", curie=MTGOC.curie('value'),
                   model_uri=MTGO.value, domain=None, range=Optional[int])

slots.ability = Slot(uri=MTGOA.ability, name="ability", curie=MTGOA.curie('ability'),
                   model_uri=MTGO.ability, domain=Card, range=Optional[Union[Union[str, AbilityId], List[Union[str, AbilityId]]]])

slots.rules_text = Slot(uri=MTGOA.rules_text, name="rules_text", curie=MTGOA.curie('rules_text'),
                   model_uri=MTGO.rules_text, domain=None, range=Optional[str])

slots.cost = Slot(uri=MTGOA.cost, name="cost", curie=MTGOA.curie('cost'),
                   model_uri=MTGO.cost, domain=None, range=Optional[Union[str, List[str]]])

slots.effect = Slot(uri=MTGOA.effect, name="effect", curie=MTGOA.curie('effect'),
                   model_uri=MTGO.effect, domain=None, range=Optional[Union[str, ConditionId]])

slots.action = Slot(uri=MTGOA.action, name="action", curie=MTGOA.curie('action'),
                   model_uri=MTGO.action, domain=None, range=Union[str, "Action"])

slots.source = Slot(uri=MTGOA.source, name="source", curie=MTGOA.curie('source'),
                   model_uri=MTGO.source, domain=None, range=Optional[str])

slots.target = Slot(uri=MTGOA.target, name="target", curie=MTGOA.curie('target'),
                   model_uri=MTGO.target, domain=None, range=Optional[str])

slots.condition = Slot(uri=MTGOA.condition, name="condition", curie=MTGOA.curie('condition'),
                   model_uri=MTGO.condition, domain=None, range=Optional[Union[str, ConditionId]])

slots.property = Slot(uri=MTGOA.property, name="property", curie=MTGOA.curie('property'),
                   model_uri=MTGO.property, domain=None, range=Optional[Union[str, PropertyId]])

slots.value_spec = Slot(uri=MTGOA.value_spec, name="value_spec", curie=MTGOA.curie('value_spec'),
                   model_uri=MTGO.value_spec, domain=None, range=Optional[Union[Union[str, ValueSpecificationId], List[Union[str, ValueSpecificationId]]]])

slots.time_spec = Slot(uri=MTGOA.time_spec, name="time_spec", curie=MTGOA.curie('time_spec'),
                   model_uri=MTGO.time_spec, domain=None, range=Optional[Union[Union[str, TimeSpecificationId], List[Union[str, TimeSpecificationId]]]])

slots.action_spec = Slot(uri=MTGOA.action_spec, name="action_spec", curie=MTGOA.curie('action_spec'),
                   model_uri=MTGO.action_spec, domain=None, range=Optional[Union[Union[str, ActionSpecificationId], List[Union[str, ActionSpecificationId]]]])

slots.player = Slot(uri=MTGOA.player, name="player", curie=MTGOA.curie('player'),
                   model_uri=MTGO.player, domain=None, range=Optional[Union[str, "Player"]])

slots.time = Slot(uri=MTGOA.time, name="time", curie=MTGOA.curie('time'),
                   model_uri=MTGO.time, domain=None, range=Optional[Union[str, "Time"]])

slots.unit = Slot(uri=MTGOA.unit, name="unit", curie=MTGOA.curie('unit'),
                   model_uri=MTGO.unit, domain=None, range=Optional[str])

slots.constraint = Slot(uri=MTGOA.constraint, name="constraint", curie=MTGOA.curie('constraint'),
                   model_uri=MTGO.constraint, domain=None, range=Optional[str])

slots.cardCollection__entries = Slot(uri=MTGOC.entries, name="cardCollection__entries", curie=MTGOC.curie('entries'),
                   model_uri=MTGO.cardCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, CardId], Union[dict, Card]], List[Union[dict, Card]]]])

slots.Cost_and = Slot(uri=MTGO.and, name="Cost_and", curie=MTGO.curie('and'),
                   model_uri=MTGO.Cost_and, domain=Cost, range=Optional[Union[str, CostId]])

slots.Cost_or = Slot(uri=MTGO.or, name="Cost_or", curie=MTGO.curie('or'),
                   model_uri=MTGO.Cost_or, domain=Cost, range=Optional[Union[str, CostId]])

slots.ActionSpecification_and = Slot(uri=MTGO.and, name="ActionSpecification_and", curie=MTGO.curie('and'),
                   model_uri=MTGO.ActionSpecification_and, domain=ActionSpecification, range=Optional[Union[str, ActionSpecificationId]])

slots.ActionSpecification_or = Slot(uri=MTGO.or, name="ActionSpecification_or", curie=MTGO.curie('or'),
                   model_uri=MTGO.ActionSpecification_or, domain=ActionSpecification, range=Optional[Union[str, ActionSpecificationId]])

slots.ActionSpecification_constraint = Slot(uri=MTGOA.constraint, name="ActionSpecification_constraint", curie=MTGOA.curie('constraint'),
                   model_uri=MTGO.ActionSpecification_constraint, domain=ActionSpecification, range=Optional[Union[str, "ActionConstraint"]])

slots.ValueSpecification_and = Slot(uri=MTGO.and, name="ValueSpecification_and", curie=MTGO.curie('and'),
                   model_uri=MTGO.ValueSpecification_and, domain=ValueSpecification, range=Optional[Union[str, ValueSpecificationId]])

slots.ValueSpecification_or = Slot(uri=MTGO.or, name="ValueSpecification_or", curie=MTGO.curie('or'),
                   model_uri=MTGO.ValueSpecification_or, domain=ValueSpecification, range=Optional[Union[str, ValueSpecificationId]])

slots.ValueSpecification_constraint = Slot(uri=MTGOA.constraint, name="ValueSpecification_constraint", curie=MTGOA.curie('constraint'),
                   model_uri=MTGO.ValueSpecification_constraint, domain=ValueSpecification, range=Optional[Union[str, "ValueConstraint"]])

slots.TimeSpecification_and = Slot(uri=MTGO.and, name="TimeSpecification_and", curie=MTGO.curie('and'),
                   model_uri=MTGO.TimeSpecification_and, domain=TimeSpecification, range=Optional[Union[str, TimeSpecificationId]])

slots.TimeSpecification_or = Slot(uri=MTGO.or, name="TimeSpecification_or", curie=MTGO.curie('or'),
                   model_uri=MTGO.TimeSpecification_or, domain=TimeSpecification, range=Optional[Union[str, TimeSpecificationId]])

slots.TimeSpecification_constraint = Slot(uri=MTGOA.constraint, name="TimeSpecification_constraint", curie=MTGOA.curie('constraint'),
                   model_uri=MTGO.TimeSpecification_constraint, domain=TimeSpecification, range=Optional[Union[str, "TimeConstraint"]])