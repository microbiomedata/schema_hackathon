## Add your own custom Makefile targets here

FORCE_DIR_MSG="forces creation of this directory"

.PHONY: sheets_all sheets_clean

sheets_all: sheets_clean src/linkml/schema_hackathon.yaml

sheets_clean:
	rm -rf schemasheets-related/output/nmdc_hackathon_schema.yaml
	rm -rf assets/*
	mkdir -p assets
	echo $(FORCE_DIR_MSG) > assets/READEME.md
	rm -rf downloads/*
	mkdir -p downloads
	echo $(FORCE_DIR_MSG) > downloads/READEME.md
	rm -rf src/linkml/schema_hackathon.yaml
	mkdir -p src/linkml
	echo $(FORCE_DIR_MSG) > src/linkml/READEME.md
	rm -rf docs/*
	mkdir -p docs
	echo $(FORCE_DIR_MSG) > docs/READEME.md

src/linkml/schema_hackathon.yaml:
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
		schema prefixes classes_slots

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