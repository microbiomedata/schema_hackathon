

CREATE TABLE "MaterialContainer" (
	container_type VARCHAR(17) NOT NULL, 
	size TEXT NOT NULL, 
	PRIMARY KEY (container_type, size)
);

CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "QuantityValue" (
	has_value FLOAT NOT NULL, 
	has_unit TEXT NOT NULL, 
	PRIMARY KEY (has_value, has_unit)
);

CREATE TABLE "Shaker" (
	shake_speed TEXT, 
	shake_time TEXT, 
	shaker_type VARCHAR(7), 
	PRIMARY KEY (shake_speed, shake_time, shaker_type)
);

CREATE TABLE "Dissolving" (
	material_input TEXT NOT NULL, 
	material_output TEXT NOT NULL, 
	container TEXT NOT NULL, 
	shaker_selection TEXT NOT NULL, 
	solvent VARCHAR(15) NOT NULL, 
	volume TEXT NOT NULL, 
	PRIMARY KEY (material_input, material_output, container, shaker_selection, solvent, volume), 
	FOREIGN KEY(material_input) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(material_output) REFERENCES "NamedThing" (id)
);

CREATE TABLE "MatSampProc" (
	collected_into TEXT NOT NULL, 
	material_input TEXT NOT NULL, 
	material_output TEXT NOT NULL, 
	amount TEXT NOT NULL, 
	PRIMARY KEY (collected_into, material_input, material_output, amount), 
	FOREIGN KEY(material_input) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(material_output) REFERENCES "NamedThing" (id)
);
