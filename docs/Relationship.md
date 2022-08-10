# Class: Relationship




URI: [my_datamodel:Relationship](https://w3id.org/my_org/my_datamodelRelationship)




```mermaid
 classDiagram
      Relationship <|-- FamilialRelationship
      
      Relationship : ended_at_time
      Relationship : related_to
      Relationship : started_at_time
      Relationship : type
      
```





## Inheritance
* **Relationship**
    * [FamilialRelationship](FamilialRelationship.md)



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [started_at_time](started_at_time.md) | 0..1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date)  |   |
| [ended_at_time](ended_at_time.md) | 0..1 <br/> [xsd:date](http://www.w3.org/2001/XMLSchema#date)  |   |
| [related_to](related_to.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [type](type.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my_org/my_datamodel







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['my_datamodel:Relationship'] |
| native | ['my_datamodel:Relationship'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Relationship
from_schema: https://w3id.org/my_org/my_datamodel
rank: 1000
slots:
- started_at_time
- ended_at_time
- related_to
- type

```
</details>

### Induced

<details>
```yaml
name: Relationship
from_schema: https://w3id.org/my_org/my_datamodel
rank: 1000
attributes:
  started_at_time:
    name: started_at_time
    from_schema: https://w3id.org/my_org/my_datamodel
    rank: 1000
    slot_uri: prov:startedAtTime
    alias: started_at_time
    owner: Relationship
    domain_of:
    - Relationship
    range: date
  ended_at_time:
    name: ended_at_time
    from_schema: https://w3id.org/my_org/my_datamodel
    rank: 1000
    slot_uri: prov:endedAtTime
    alias: ended_at_time
    owner: Relationship
    domain_of:
    - Relationship
    range: date
  related_to:
    name: related_to
    from_schema: https://w3id.org/my_org/my_datamodel
    rank: 1000
    alias: related_to
    owner: Relationship
    domain_of:
    - Relationship
    range: string
  type:
    name: type
    from_schema: https://w3id.org/my_org/my_datamodel
    rank: 1000
    alias: type
    owner: Relationship
    domain_of:
    - Relationship
    range: string

```
</details>