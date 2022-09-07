
# monet_schema


**metamodel version:** 1.7.0

**version:** None


A sandbox for modeling MONET sample processing activities


### Classes

 * [DissolvingProcess](DissolvingProcess.md)
 * [LabDevice](LabDevice.md)
 * [MaterialContainer](MaterialContainer.md)
 * [MaterialSamplingProcess](MaterialSamplingProcess.md)
 * [NamedThing](NamedThing.md)
     * [Database](Database.md)
     * [MaterialSample](MaterialSample.md)
 * [QuantityValue](QuantityValue.md)
 * [ReactionActivity](ReactionActivity.md)

### Mixins


### Slots

 * [amount_collected](amount_collected.md)
 * [collected_into](collected_into.md)
 * [container_size](container_size.md)
 * [container_type](container_type.md)
 * [description](description.md)
 * [device_type](device_type.md)
 * [dissolution_aided_by](dissolution_aided_by.md)
 * [dissolution_reagent](dissolution_reagent.md)
 * [dissolution_volume](dissolution_volume.md)
 * [dissolved_in](dissolved_in.md)
 * [dissolving_process_set](dissolving_process_set.md)
 * [has_unit](has_unit.md)
 * [has_value](has_value.md)
 * [id](id.md)
 * [material_input](material_input.md)
 * [material_output](material_output.md)
 * [material_sample_set](material_sample_set.md)
 * [material_sampling_process_set](material_sampling_process_set.md)
 * [process_speed](process_speed.md)
 * [process_temperature](process_temperature.md)
 * [process_time](process_time.md)
 * [reaction_activity_set](reaction_activity_set.md)
 * [reaction_aided_by](reaction_aided_by.md)
 * [reaction_temperature](reaction_temperature.md)
 * [reaction_time](reaction_time.md)
 * [sampling_method](sampling_method.md)

### Enums

 * [ContainerTypeEnum](ContainerTypeEnum.md)
 * [DeviceTypeEnum](DeviceTypeEnum.md)
 * [SamplingMethodEnum](SamplingMethodEnum.md)
 * [SolventEnum](SolventEnum.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
