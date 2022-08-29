# Class: MatSampProc




URI: [OBI:0000744](http://purl.obolibrary.org/obo/OBI_0000744)




```mermaid
 classDiagram
    class MatSampProc
      MatSampProc : amount
      MatSampProc : collected_into
      MatSampProc : material_input
      MatSampProc : material_output
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [amount](amount.md) | 1..1 <br/> [QuantityValue](QuantityValue.md)  |   |
| [collected_into](collected_into.md) | 1..1 <br/> [MaterialContainer](MaterialContainer.md)  |   |
| [material_input](material_input.md) | 1..1 <br/> [NamedThing](NamedThing.md)  |   |
| [material_output](material_output.md) | 1..1 <br/> [NamedThing](NamedThing.md)  |   |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: http://example.com/monet_schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['OBI:0000744'] |
| native | ['monet_schema:MatSampProc'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MatSampProc
title: Material sampling process
from_schema: http://example.com/monet_schema
aliases:
- weighing-activity
rank: 1000
slots:
- amount
- collected_into
- material_input
- material_output
class_uri: OBI:0000744

```
</details>

### Induced

<details>
```yaml
name: MatSampProc
title: Material sampling process
from_schema: http://example.com/monet_schema
aliases:
- weighing-activity
rank: 1000
attributes:
  amount:
    name: amount
    title: amount
    from_schema: http://example.com/monet_schema
    rank: 1000
    alias: amount
    owner: MatSampProc
    domain_of:
    - MatSampProc
    range: QuantityValue
    required: true
    inlined: true
    inlined_as_list: true
  collected_into:
    name: collected_into
    title: collected into
    from_schema: http://example.com/monet_schema
    rank: 1000
    alias: collected_into
    owner: MatSampProc
    domain_of:
    - MatSampProc
    range: MaterialContainer
    required: true
    inlined: true
    inlined_as_list: true
  material_input:
    name: material_input
    examples:
    - value: soil:1
    from_schema: http://example.com/monet_schema
    aliases:
    - weighing-activity.source_material
    rank: 1000
    alias: material_input
    owner: MatSampProc
    domain_of:
    - MatSampProc
    range: NamedThing
    required: true
    inlined: true
    inlined_as_list: true
  material_output:
    name: material_output
    examples:
    - value: somextract:6
    from_schema: http://example.com/monet_schema
    aliases:
    - weighing-activity.id
    rank: 1000
    alias: material_output
    owner: MatSampProc
    domain_of:
    - MatSampProc
    range: NamedThing
    required: true
    inlined: true
    inlined_as_list: true
class_uri: OBI:0000744

```
</details>