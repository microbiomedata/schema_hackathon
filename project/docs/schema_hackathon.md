
# monet_schema


**metamodel version:** 1.7.0

**version:** None


A sandbox for modeling MONET sample processing activities


### Classes

 * [Dissolving](Dissolving.md)
 * [MatSampProc](MatSampProc.md)
 * [MaterialContainer](MaterialContainer.md)
 * [NamedThing](NamedThing.md)
     * [MaterialEntity](MaterialEntity.md)
 * [QuantityValue](QuantityValue.md)
 * [Shaker](Shaker.md)

### Mixins


### Slots

 * [amount](amount.md)
 * [collected_into](collected_into.md)
 * [container](container.md)
 * [container_type](container_type.md)
 * [has_unit](has_unit.md)
 * [has_value](has_value.md)
 * [id](id.md)
 * [material_input](material_input.md)
 * [material_output](material_output.md)
 * [shake_speed](shake_speed.md)
 * [shake_time](shake_time.md)
 * [shaker_selection](shaker_selection.md)
 * [shaker_type](shaker_type.md)
 * [size](size.md)
 * [solvent](solvent.md)
 * [volume](volume.md)

### Enums

 * [ContainerTypeEnum](ContainerTypeEnum.md)
 * [ShakerTypeEnum](ShakerTypeEnum.md)
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
