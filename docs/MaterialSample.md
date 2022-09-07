# Class: MaterialSample




URI: [monet_schema:MaterialSample](http://example.com/monet_schema/MaterialSample)




```mermaid
 classDiagram
      NamedThing <|-- MaterialSample
      
      MaterialSample : description
      MaterialSample : id
      

```





## Inheritance
* [NamedThing](NamedThing.md)
    * **MaterialSample**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [description](description.md) | 0..1 <br/> [xsd:string](xsd:string)  |   |
| [id](id.md) | 1..1 <br/> [xsd:string](xsd:string)  |   |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Database](Database.md) | [material_sample_set](material_sample_set.md) | range | MaterialSample |
| [DissolvingProcess](DissolvingProcess.md) | [material_input](material_input.md) | range | MaterialSample |
| [DissolvingProcess](DissolvingProcess.md) | [material_output](material_output.md) | range | MaterialSample |
| [MaterialSamplingProcess](MaterialSamplingProcess.md) | [material_input](material_input.md) | range | MaterialSample |
| [MaterialSamplingProcess](MaterialSamplingProcess.md) | [material_output](material_output.md) | range | MaterialSample |
| [ReactionActivity](ReactionActivity.md) | [material_input](material_input.md) | range | MaterialSample |
| [ReactionActivity](ReactionActivity.md) | [material_output](material_output.md) | range | MaterialSample |



## Identifier and Mapping Information







### Schema Source


* from schema: http://example.com/monet_schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['monet_schema:MaterialSample'] |
| native | ['monet_schema:MaterialSample'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaterialSample
title: Material sample
from_schema: http://example.com/monet_schema
aliases:
- Material entity
rank: 1000
is_a: NamedThing

```
</details>

### Induced

<details>
```yaml
name: MaterialSample
title: Material sample
from_schema: http://example.com/monet_schema
aliases:
- Material entity
rank: 1000
is_a: NamedThing
attributes:
  description:
    name: description
    title: description
    from_schema: http://example.com/monet_schema
    rank: 1000
    alias: description
    owner: MaterialSample
    domain_of:
    - NamedThing
    range: string
  id:
    name: id
    from_schema: http://example.com/monet_schema
    rank: 1000
    identifier: true
    alias: id
    owner: MaterialSample
    domain_of:
    - NamedThing
    range: string

```
</details>