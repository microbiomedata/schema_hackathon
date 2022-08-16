

CREATE TABLE "Human" (
	eye_color TEXT, 
	human_full_name TEXT, 
	PRIMARY KEY (eye_color, human_full_name)
);

CREATE TABLE "Mammal" (
	eye_color TEXT, 
	PRIMARY KEY (eye_color)
);
