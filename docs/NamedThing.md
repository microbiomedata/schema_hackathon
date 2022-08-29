# Class: NamedThing




URI: [monet_schema:NamedThing](http://example.com/monet_schema/NamedThing)




```mermaid
 classDiagram
      NamedThing <|-- MaterialEntity
      
      NamedThing : id
      
```





## Inheritance
* **NamedThing**
    * [MaterialEntity](MaterialEntity.md)



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [id](id.md) | 1..1 <br/> [xsd:string](xsd:string)  |   |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MatSampProc](MatSampProc.md) | [material_input](material_input.md) | range | NamedThing |
| [MatSampProc](MatSampProc.md) | [material_output](material_output.md) | range | NamedThing |



## Identifier and Mapping Information







### Schema Source


* from schema: http://example.com/monet_schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['monet_schema:NamedThing'] |
| native | ['monet_schema:NamedThing'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NamedThing
from_schema: http://example.com/monet_schema
rank: 1000
slots:
- id

```
</details>

### Induced

<details>
```yaml
name: NamedThing
from_schema: http://example.com/monet_schema
rank: 1000
attributes:
  id:
    name: id
    from_schema: http://example.com/monet_schema
    rank: 1000
    identifier: true
    alias: id
    owner: NamedThing
    domain_of:
    - NamedThing
    range: string
    required: true

```
</details>