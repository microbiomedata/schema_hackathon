## Add your own custom Makefile targets here

FORCE_DIR_MSG="forces creation of this directory"

DOCDIR = docs
SRC = src
RUN=poetry run
SOURCE_SCHEMA_PATH = $(shell sh ./utils/get-value.sh source_schema_path)

.PHONY: sheets_all sheets_clean

sheets_all: sheets_clean src/linkml/schema_hackathon_generated.yaml src/data/examples/weighing_data.json src/data/examples/dissolving_data.json

sheets_clean:
	rm -rf schemasheets-related/output/nmdc_hackathon_schema.yaml
	rm -rf assets/*
	rm -rf assets/*
	mkdir -p assets
	echo $(FORCE_DIR_MSG) > assets/README.md
	rm -rf downloads/*
	mkdir -p downloads
	echo $(FORCE_DIR_MSG) > downloads/README.md
	rm -rf src/linkml/schema_hackathon.yaml
	mkdir -p src/linkml
	echo $(FORCE_DIR_MSG) > src/linkml/README.md
	rm -rf docs/*
	mkdir -p docs
	echo $(FORCE_DIR_MSG) > docs/README.md
	rm -rf src/data/examples/dissolving_data.json src/data/examples/weighing_data.json src/linkml/schema_hackathon.yaml src/linkml/schema_hackathon_generated.yaml

src/linkml/schema_hackathon.yaml: sheets_clean
	# --unique-slots / --no-unique-slots (default)
	# --repair (default) / --no-repair
	# note booleans and numbers vs strings
	# could also take input from TSVs
	# sheets must be at least world readable
	# (but can't cogs be used in an authenticated mode?)
	# --verbose spews out the LinkML language definition ?!
	# note there are various ways to associate a slot with a class in schemasheets
	#   many of those create a minimal slot_usage
	# needs either
	#   --name nmdc_hackathon_schema
	# or a schema definition sheet
	# imports linkml:types by default and defines the linkml prefix
	# sets the default_range to string
	$(RUN) sheets2linkml \
		--gsheet-id 1sYpMyhCMzL6-JyvA6qlczf_vtNWybmuPvwoeqMUUiNo \
		--output $@ \
		--unique-slots \
		--no-repair \
		monet \
		monet_enums \
		monet_prefixes \
		monet_schema

src/linkml/schema_hackathon_generated.yaml: src/linkml/schema_hackathon.yaml
	$(RUN) gen-linkml \
		--format yaml \
		--no-materialize-attributes $< > $@


src/data/examples/weighing_data.json: src/data/examples/weighing_data.yaml src/linkml/schema_hackathon_generated.yaml
	$(RUN) linkml-convert -s src/linkml/schema_hackathon_generated.yaml -C MaterialSamplingProcess $< -o $@

src/data/examples/dissolving_data.json: src/data/examples/dissolving_data.yaml src/linkml/schema_hackathon_generated.yaml
	$(RUN) linkml-convert -s src/linkml/schema_hackathon_generated.yaml -C DissolvingProcess $< -o $@

#src/data/examples/named_thing_data.json: src/data/examples/named_thing_data.yaml src/linkml/schema_hackathon_generated.yaml
#	$(RUN) linkml-convert -s src/linkml/schema_hackathon_generated.yaml -C NamedThing $< -o $@

#src/data/examples/named_thing_database.json: src/data/examples/named_thing_database.yaml src/linkml/schema_hackathon_generated.yaml
#	$(RUN) linkml-convert -s src/linkml/schema_hackathon_generated.yaml -C Database $< -o $@

src/data/examples/multi_class_database.json: src/data/examples/multi_class_database.yaml src/linkml/schema_hackathon_generated.yaml
	$(RUN) linkml-convert -s src/linkml/schema_hackathon_generated.yaml -C Database $< -o $@

src/data/examples/reaction_data.json: src/data/examples/reaction_data.yaml src/linkml/schema_hackathon_generated.yaml
	$(RUN) linkml-convert -s src/linkml/schema_hackathon_generated.yaml -C ReactionActivity $< -o $@



#src/data/examples/weigh_dissolve_database.ttl: src/data/examples/multi_class_database.yaml src/linkml/schema_hackathon_generated.yaml
#	$(RUN) linkml-convert -s src/linkml/schema_hackathon_generated.yaml -C Database $< -o $@
#
#src/linkml/schema_hackathon.ttl: src/linkml/schema_hackathon.yaml
#	$(RUN) gen-owl \
#		--output $@ \
#		--metadata-profile rdfs \
#		--no-type-objects \
#		--no-metaclasses \
#		--no-add-ols-annotations \
#		--no-metadata  $<


schemasheets-related/output/nmdc_hackathon_schema.schema.json: schemasheets-related/output/nmdc_hackathon_schema.yaml
	$(RUN) gen-json-schema \
		--closed \
		$< > $@


# initial populated class/slot sheet from wizard
# via target/output/NMDC_schema_slot_class_merged_with_filtered_rels.tsv rule in
# https://github.com/linkml/schemasheets/blob/<branch/commit>>/template_wizard.Makefile
assets/NMDC_schema_slot_class_merged_with_filtered_rels.csv: assets/NMDC_schema_slot_class_merged_with_filtered_rels.tsv
	$(RUN) python schema_hackathon/tsv_to_csv.py < $< > $@

# NMDC biosample or study slots DRAFT
downloads/mls_curated_nmdc_class_slot_sheet_pop.csv:
	curl -L "https://docs.google.com/spreadsheets/d/1A8FN8rymVI9N1Yv0dMlV2RCbrVKWUvYyDOZssmy8LEc/export?gid=1025122986&format=csv" > $@

highlight_curations: assets/NMDC_schema_slot_class_merged_with_filtered_rels.csv downloads/mls_curated_nmdc_class_slot_sheet_pop.csv
	csvdiff $^ --primary-key  1,2 --format word-diff
	# (rowmark|json|legacy-json|diff|word-diff|color-words) (default "diff")

# Sujay and Mark experimenting with explicit Jinja2 templates

#$(DOCDIR):
#	mkdir -p $@

# todo parameterize the templates directory ?
templated_gendoc: $(DOCDIR)
	cp $(SRC)/docs/*md $(DOCDIR) ; \
	$(RUN) gen-doc -d $(DOCDIR) --template-directory doc_templates $(SOURCE_SCHEMA_PATH)