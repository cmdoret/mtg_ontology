

CREATE TABLE "AbilityCollection" (
	activated_abilities TEXT, 
	conditions TEXT, 
	mana_costs TEXT, 
	value_specifications TEXT, 
	action_specifications TEXT, 
	time_specifications TEXT, 
	PRIMARY KEY (activated_abilities, conditions, mana_costs, value_specifications, action_specifications, time_specifications)
);

CREATE TABLE "ActionSpecification" (
	id TEXT NOT NULL, 
	action VARCHAR(11) NOT NULL, 
	intersection TEXT, 
	"union" TEXT, 
	"constraint" VARCHAR(8), 
	PRIMARY KEY (id), 
	FOREIGN KEY(intersection) REFERENCES "ActionSpecification" (id), 
	FOREIGN KEY("union") REFERENCES "ActionSpecification" (id)
);

CREATE TABLE "Artifact" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	mana_cost TEXT, 
	converted_mana_cost INTEGER, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	rarity VARCHAR(8), 
	oracle_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ArtifactToken" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	oracle_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "CardCollection" (
	cards TEXT, 
	costs TEXT, 
	PRIMARY KEY (cards, costs)
);

CREATE TABLE "Condition" (
	id TEXT NOT NULL, 
	source TEXT, 
	target TEXT, 
	action_spec TEXT, 
	value_spec TEXT, 
	time_spec TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Cost" (
	id TEXT NOT NULL, 
	value INTEGER, 
	intersection TEXT, 
	"union" TEXT, 
	variable_cost BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(intersection) REFERENCES "Cost" (id), 
	FOREIGN KEY("union") REFERENCES "Cost" (id)
);

CREATE TABLE "Counter" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Creature" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	mana_cost TEXT, 
	converted_mana_cost INTEGER, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	rarity VARCHAR(8), 
	oracle_text TEXT, 
	power INTEGER NOT NULL, 
	toughness INTEGER NOT NULL, 
	variable_power BOOLEAN, 
	variable_toughness BOOLEAN, 
	PRIMARY KEY (id)
);

CREATE TABLE "CreatureToken" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	oracle_text TEXT, 
	power INTEGER NOT NULL, 
	toughness INTEGER NOT NULL, 
	variable_power BOOLEAN, 
	variable_toughness BOOLEAN, 
	PRIMARY KEY (id)
);

CREATE TABLE "Enchantment" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	mana_cost TEXT, 
	converted_mana_cost INTEGER, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	rarity VARCHAR(8), 
	oracle_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "EnchantmentToken" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	oracle_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Instant" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	mana_cost TEXT, 
	converted_mana_cost INTEGER, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	rarity VARCHAR(8), 
	oracle_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "KeywordCounter" (
	id TEXT NOT NULL, 
	ability_keyword TEXT, 
	value_spec TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Land" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	mana_cost TEXT, 
	converted_mana_cost INTEGER, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	rarity VARCHAR(8), 
	oracle_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Mana" (
	id TEXT NOT NULL, 
	snow BOOLEAN, 
	phyrexian BOOLEAN, 
	hybrid BOOLEAN, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PowerToughnessCounter" (
	id TEXT NOT NULL, 
	power_modifier INTEGER, 
	toughness_modifier INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE "Sorcery" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	mana_cost TEXT, 
	converted_mana_cost INTEGER, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	rarity VARCHAR(8), 
	oracle_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Spell" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Thing" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "TimeSpecification" (
	id TEXT NOT NULL, 
	turn_phase VARCHAR(24), 
	player VARCHAR(17), 
	intersection TEXT, 
	"union" TEXT, 
	"constraint" VARCHAR(8), 
	PRIMARY KEY (id), 
	FOREIGN KEY(intersection) REFERENCES "TimeSpecification" (id), 
	FOREIGN KEY("union") REFERENCES "TimeSpecification" (id)
);

CREATE TABLE "Token" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	card_set TEXT, 
	artist TEXT, 
	flavor_text TEXT, 
	type_line TEXT NOT NULL, 
	card_type TEXT NOT NULL, 
	oracle_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ValueSpecification" (
	id TEXT NOT NULL, 
	value INTEGER, 
	unit TEXT, 
	intersection TEXT, 
	"union" TEXT, 
	"constraint" VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(intersection) REFERENCES "ValueSpecification" (id), 
	FOREIGN KEY("union") REFERENCES "ValueSpecification" (id)
);

CREATE TABLE "ActivatedAbility" (
	id TEXT NOT NULL, 
	rules_text TEXT, 
	effect TEXT, 
	ability_keyword TEXT, 
	condition TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(effect) REFERENCES "Condition" (id), 
	FOREIGN KEY(condition) REFERENCES "Condition" (id)
);

CREATE TABLE "LifeCost" (
	id TEXT NOT NULL, 
	value INTEGER, 
	intersection TEXT, 
	"union" TEXT, 
	variable_cost BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(intersection) REFERENCES "Cost" (id), 
	FOREIGN KEY("union") REFERENCES "Cost" (id)
);

CREATE TABLE "ManaCost" (
	id TEXT NOT NULL, 
	value INTEGER, 
	intersection TEXT, 
	"union" TEXT, 
	variable_cost BOOLEAN, 
	snow BOOLEAN, 
	phyrexian BOOLEAN, 
	hybrid BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(intersection) REFERENCES "Cost" (id), 
	FOREIGN KEY("union") REFERENCES "Cost" (id)
);

CREATE TABLE "StaticAbility" (
	id TEXT NOT NULL, 
	rules_text TEXT, 
	effect TEXT, 
	ability_keyword TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(effect) REFERENCES "Condition" (id)
);

CREATE TABLE "TriggeredAbility" (
	id TEXT NOT NULL, 
	rules_text TEXT, 
	effect TEXT, 
	ability_keyword TEXT, 
	condition TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(effect) REFERENCES "Condition" (id), 
	FOREIGN KEY(condition) REFERENCES "Condition" (id)
);

CREATE TABLE "Artifact_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Artifact" (id)
);

CREATE TABLE "Artifact_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "Artifact" (id)
);

CREATE TABLE "Artifact_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "Artifact" (id)
);

CREATE TABLE "Artifact_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "Artifact" (id)
);

CREATE TABLE "ArtifactToken_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "ArtifactToken" (id)
);

CREATE TABLE "ArtifactToken_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "ArtifactToken" (id)
);

CREATE TABLE "ArtifactToken_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "ArtifactToken" (id)
);

CREATE TABLE "ArtifactToken_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "ArtifactToken" (id)
);

CREATE TABLE "Creature_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Creature" (id)
);

CREATE TABLE "Creature_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "Creature" (id)
);

CREATE TABLE "Creature_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "Creature" (id)
);

CREATE TABLE "Creature_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "Creature" (id)
);

CREATE TABLE "CreatureToken_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "CreatureToken" (id)
);

CREATE TABLE "CreatureToken_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "CreatureToken" (id)
);

CREATE TABLE "CreatureToken_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "CreatureToken" (id)
);

CREATE TABLE "CreatureToken_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "CreatureToken" (id)
);

CREATE TABLE "Enchantment_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Enchantment" (id)
);

CREATE TABLE "Enchantment_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "Enchantment" (id)
);

CREATE TABLE "Enchantment_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "Enchantment" (id)
);

CREATE TABLE "Enchantment_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "Enchantment" (id)
);

CREATE TABLE "EnchantmentToken_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "EnchantmentToken" (id)
);

CREATE TABLE "EnchantmentToken_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "EnchantmentToken" (id)
);

CREATE TABLE "EnchantmentToken_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "EnchantmentToken" (id)
);

CREATE TABLE "EnchantmentToken_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "EnchantmentToken" (id)
);

CREATE TABLE "Instant_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Instant" (id)
);

CREATE TABLE "Instant_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "Instant" (id)
);

CREATE TABLE "Instant_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "Instant" (id)
);

CREATE TABLE "Instant_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "Instant" (id)
);

CREATE TABLE "Land_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Land" (id)
);

CREATE TABLE "Land_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "Land" (id)
);

CREATE TABLE "Land_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "Land" (id)
);

CREATE TABLE "Land_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "Land" (id)
);

CREATE TABLE "Mana_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Mana" (id)
);

CREATE TABLE "Sorcery_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Sorcery" (id)
);

CREATE TABLE "Sorcery_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "Sorcery" (id)
);

CREATE TABLE "Sorcery_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "Sorcery" (id)
);

CREATE TABLE "Sorcery_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "Sorcery" (id)
);

CREATE TABLE "Token_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Token" (id)
);

CREATE TABLE "Token_ability" (
	backref_id TEXT, 
	ability TEXT, 
	PRIMARY KEY (backref_id, ability), 
	FOREIGN KEY(backref_id) REFERENCES "Token" (id)
);

CREATE TABLE "Token_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "Token" (id)
);

CREATE TABLE "Token_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "Token" (id)
);

CREATE TABLE "ActivatedAbility_cost" (
	backref_id TEXT, 
	cost TEXT, 
	PRIMARY KEY (backref_id, cost), 
	FOREIGN KEY(backref_id) REFERENCES "ActivatedAbility" (id)
);

CREATE TABLE "ManaCost_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "ManaCost" (id)
);
