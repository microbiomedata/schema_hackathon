

CREATE TABLE "MaterialContainer" (
	container_type TEXT NOT NULL, 
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
	has_unit TEXT NOT NULL, 
	has_value FLOAT NOT NULL, 
	PRIMARY KEY (has_unit, has_value)
);

CREATE TABLE "MatSampProc" (
	amount TEXT NOT NULL, 
	collected_into TEXT NOT NULL, 
	material_input TEXT NOT NULL, 
	material_output TEXT NOT NULL, 
	PRIMARY KEY (amount, collected_into, material_input, material_output), 
	FOREIGN KEY(material_input) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(material_output) REFERENCES "NamedThing" (id)
);
