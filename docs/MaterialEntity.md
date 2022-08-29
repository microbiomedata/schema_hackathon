# Class: MaterialEntity




URI: [monet_schema:MaterialEntity](http://example.com/monet_schema/MaterialEntity)




```mermaid
 classDiagram
      NamedThing <|-- MaterialEntity
      
      MaterialEntity : id
      

```





## Inheritance
* [NamedThing](NamedThing.md)
    * **MaterialEntity**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [id](id.md) | 1..1 <br/> [xsd:string](xsd:string)  |   |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: http://example.com/monet_schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['monet_schema:MaterialEntity'] |
| native | ['monet_schema:MaterialEntity'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaterialEntity
title: Material entity
from_schema: http://example.com/monet_schema
rank: 1000
is_a: NamedThing

```
</details>

### Induced

<details>
```yaml
name: MaterialEntity
title: Material entity
from_schema: http://example.com/monet_schema
rank: 1000
is_a: NamedThing
attributes:
  id:
    name: id
    from_schema: http://example.com/monet_schema
    rank: 1000
    identifier: true
    alias: id
    owner: MaterialEntity
    domain_of:
    - NamedThing
    range: string
    required: true

```
</details>