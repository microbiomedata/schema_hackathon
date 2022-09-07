

CREATE TABLE "Database" (
	description TEXT, 
	id TEXT NOT NULL, 
	material_sample_set TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "LabDevice" (
	device_type VARCHAR(14), 
	process_speed TEXT, 
	process_temperature TEXT, 
	process_time TEXT, 
	PRIMARY KEY (device_type, process_speed, process_temperature, process_time)
);

CREATE TABLE "MaterialContainer" (
	container_size TEXT, 
	container_type VARCHAR(17), 
	PRIMARY KEY (container_size, container_type)
);

CREATE TABLE "MaterialSample" (
	description TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	description TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "QuantityValue" (
	has_value FLOAT, 
	has_unit TEXT, 
	PRIMARY KEY (has_value, has_unit)
);

CREATE TABLE "DissolvingProcess" (
	material_input TEXT, 
	material_output TEXT, 
	dissolution_aided_by TEXT, 
	dissolution_reagent VARCHAR(15), 
	dissolution_volume TEXT, 
	dissolved_in TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (material_input, material_output, dissolution_aided_by, dissolution_reagent, dissolution_volume, dissolved_in, "Database_id"), 
	FOREIGN KEY(material_input) REFERENCES "MaterialSample" (id), 
	FOREIGN KEY(material_output) REFERENCES "MaterialSample" (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "MaterialSamplingProcess" (
	collected_into TEXT, 
	material_input TEXT, 
	material_output TEXT, 
	amount_collected TEXT, 
	sampling_method VARCHAR(8), 
	"Database_id" TEXT, 
	PRIMARY KEY (collected_into, material_input, material_output, amount_collected, sampling_method, "Database_id"), 
	FOREIGN KEY(material_input) REFERENCES "MaterialSample" (id), 
	FOREIGN KEY(material_output) REFERENCES "MaterialSample" (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);

CREATE TABLE "ReactionActivity" (
	material_input TEXT, 
	material_output TEXT, 
	reaction_time TEXT, 
	reaction_aided_by TEXT, 
	reaction_temperature TEXT, 
	"Database_id" TEXT, 
	PRIMARY KEY (material_input, material_output, reaction_time, reaction_aided_by, reaction_temperature, "Database_id"), 
	FOREIGN KEY(material_input) REFERENCES "MaterialSample" (id), 
	FOREIGN KEY(material_output) REFERENCES "MaterialSample" (id), 
	FOREIGN KEY("Database_id") REFERENCES "Database" (id)
);
