

CREATE TABLE "ActionSpecification" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	action VARCHAR(14) NOT NULL, 
	"and" TEXT, 
	"or" TEXT, 
	"constraint" VARCHAR(8), 
	PRIMARY KEY (id), 
	FOREIGN KEY("and") REFERENCES "ActionSpecification" (id), 
	FOREIGN KEY("or") REFERENCES "ActionSpecification" (id)
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
	PRIMARY KEY (id)
);

CREATE TABLE "Card" (
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
	PRIMARY KEY (id)
);

CREATE TABLE "CardCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "Cost" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	value INTEGER, 
	"and" TEXT, 
	"or" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("and") REFERENCES "Cost" (id), 
	FOREIGN KEY("or") REFERENCES "Cost" (id)
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
	power INTEGER NOT NULL, 
	toughness INTEGER NOT NULL, 
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
	PRIMARY KEY (id)
);

CREATE TABLE "Mana" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	snow BOOLEAN, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Permanent" (
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
	PRIMARY KEY (id)
);

CREATE TABLE "Property" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
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
	PRIMARY KEY (id)
);

CREATE TABLE "Spell" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TimeSpecification" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	time VARCHAR(24), 
	player VARCHAR(10), 
	"and" TEXT, 
	"or" TEXT, 
	"constraint" VARCHAR(8), 
	PRIMARY KEY (id), 
	FOREIGN KEY("and") REFERENCES "TimeSpecification" (id), 
	FOREIGN KEY("or") REFERENCES "TimeSpecification" (id)
);

CREATE TABLE "Token" (
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
	PRIMARY KEY (id)
);

CREATE TABLE "ValueSpecification" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	value INTEGER, 
	unit TEXT, 
	"and" TEXT, 
	"or" TEXT, 
	"constraint" VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY("and") REFERENCES "ValueSpecification" (id), 
	FOREIGN KEY("or") REFERENCES "ValueSpecification" (id)
);

CREATE TABLE "Condition" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	source TEXT, 
	target TEXT, 
	property TEXT, 
	action_spec TEXT, 
	value_spec TEXT, 
	time_spec TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(property) REFERENCES "Property" (id)
);

CREATE TABLE "LifeCost" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	value INTEGER, 
	"and" TEXT, 
	"or" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("and") REFERENCES "Cost" (id), 
	FOREIGN KEY("or") REFERENCES "Cost" (id)
);

CREATE TABLE "ManaCost" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	value INTEGER, 
	"and" TEXT, 
	"or" TEXT, 
	snow BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY("and") REFERENCES "Cost" (id), 
	FOREIGN KEY("or") REFERENCES "Cost" (id)
);

CREATE TABLE "Specification" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	"constraint" TEXT, 
	"and" TEXT, 
	"or" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("and") REFERENCES "NamedThing" (id), 
	FOREIGN KEY("or") REFERENCES "NamedThing" (id)
);

CREATE TABLE "Artifact_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
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

CREATE TABLE "Card_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Card" (id)
);

CREATE TABLE "Card_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "Card" (id)
);

CREATE TABLE "Card_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "Card" (id)
);

CREATE TABLE "Creature_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
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

CREATE TABLE "Enchantment_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
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

CREATE TABLE "Instant_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
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

CREATE TABLE "Permanent_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "Permanent" (id)
);

CREATE TABLE "Permanent_card_subtype" (
	backref_id TEXT, 
	card_subtype TEXT, 
	PRIMARY KEY (backref_id, card_subtype), 
	FOREIGN KEY(backref_id) REFERENCES "Permanent" (id)
);

CREATE TABLE "Permanent_card_supertype" (
	backref_id TEXT, 
	card_supertype TEXT, 
	PRIMARY KEY (backref_id, card_supertype), 
	FOREIGN KEY(backref_id) REFERENCES "Permanent" (id)
);

CREATE TABLE "Sorcery_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
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

CREATE TABLE "Ability" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	effect TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(effect) REFERENCES "Condition" (id)
);

CREATE TABLE "ActivatedAbility" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	effect TEXT, 
	condition TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(effect) REFERENCES "Condition" (id), 
	FOREIGN KEY(condition) REFERENCES "Condition" (id)
);

CREATE TABLE "KeywordAbility" (
	id TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	effect TEXT, 
	name TEXT NOT NULL, 
	value INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(effect) REFERENCES "Condition" (id)
);

CREATE TABLE "StaticAbility" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	effect TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(effect) REFERENCES "Condition" (id)
);

CREATE TABLE "TriggeredAbility" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	effect TEXT, 
	condition TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(effect) REFERENCES "Condition" (id), 
	FOREIGN KEY(condition) REFERENCES "Condition" (id)
);

CREATE TABLE "ManaCost_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "ManaCost" (id)
);

CREATE TABLE "ActivatedAbility_cost" (
	backref_id TEXT, 
	cost TEXT, 
	PRIMARY KEY (backref_id, cost), 
	FOREIGN KEY(backref_id) REFERENCES "ActivatedAbility" (id)
);
