# Class: NamedThing
_A generic grouping for any identifiable entity_





URI: [my_datamodel:NamedThing](https://w3id.org/my_org/my_datamodelNamedThing)




```mermaid
 classDiagram
      NamedThing <|-- Person
      NamedThing <|-- Organization
      
      NamedThing : description
      NamedThing : id
      NamedThing : image
      NamedThing : name
      
```





## Inheritance
* **NamedThing**
    * [Person](Person.md) [ HasAliases]
    * [Organization](Organization.md) [ HasAliases]



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [id](id.md) | 1..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [name](name.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [description](description.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [image](image.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my_org/my_datamodel







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['my_datamodel:NamedThing'] |
| native | ['my_datamodel:NamedThing'] |
| close | ['schema:Thing'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NamedThing
description: A generic grouping for any identifiable entity
from_schema: https://w3id.org/my_org/my_datamodel
close_mappings:
- schema:Thing
rank: 1000
slots:
- id
- name
- description
- image

```
</details>

### Induced

<details>
```yaml
name: NamedThing
description: A generic grouping for any identifiable entity
from_schema: https://w3id.org/my_org/my_datamodel
close_mappings:
- schema:Thing
rank: 1000
attributes:
  id:
    name: id
    from_schema: https://w3id.org/my_org/my_datamodel
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: NamedThing
    domain_of:
    - NamedThing
    range: string
  name:
    name: name
    from_schema: https://w3id.org/my_org/my_datamodel
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: NamedThing
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    from_schema: https://w3id.org/my_org/my_datamodel
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: NamedThing
    domain_of:
    - NamedThing
    range: string
  image:
    name: image
    from_schema: https://w3id.org/my_org/my_datamodel
    rank: 1000
    slot_uri: schema:image
    alias: image
    owner: NamedThing
    domain_of:
    - NamedThing
    range: string

```
</details>