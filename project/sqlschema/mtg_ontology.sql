

CREATE TABLE "Ability" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ActivatedAbility" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	additional_cost TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Artifact" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	ability TEXT, 
	additional_cost TEXT, 
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
	ability TEXT, 
	additional_cost TEXT, 
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
	PRIMARY KEY (id)
);

CREATE TABLE "Creature" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	ability TEXT, 
	additional_cost TEXT, 
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
	ability TEXT, 
	additional_cost TEXT, 
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

CREATE TABLE "Event" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	source TEXT, 
	action VARCHAR(11) NOT NULL, 
	target TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Instant" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	ability TEXT, 
	additional_cost TEXT, 
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

CREATE TABLE "KeywordAbility" (
	id TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	name TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Land" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	ability TEXT, 
	additional_cost TEXT, 
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

CREATE TABLE "LifeCost" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	value INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE "ManaCost" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	value INTEGER, 
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
	ability TEXT, 
	additional_cost TEXT, 
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

CREATE TABLE "Sorcery" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	ability TEXT, 
	additional_cost TEXT, 
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

CREATE TABLE "StaticAbility" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Token" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	ability TEXT, 
	additional_cost TEXT, 
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

CREATE TABLE "TriggeredAbility" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	rules_text TEXT, 
	condition TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(condition) REFERENCES "Event" (id)
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

CREATE TABLE "ManaCost_color" (
	backref_id TEXT, 
	color VARCHAR(9) NOT NULL, 
	PRIMARY KEY (backref_id, color), 
	FOREIGN KEY(backref_id) REFERENCES "ManaCost" (id)
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
