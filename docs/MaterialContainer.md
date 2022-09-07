# Class: MaterialContainer




URI: [monet_schema:MaterialContainer](http://example.com/monet_schema/MaterialContainer)




```mermaid
 classDiagram
    class MaterialContainer
      MaterialContainer : container_size
      MaterialContainer : container_type
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [container_size](container_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md)  |   |
| [container_type](container_type.md) | 0..1 <br/> [ContainerTypeEnum](ContainerTypeEnum.md)  |   |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DissolvingProcess](DissolvingProcess.md) | [dissolved_in](dissolved_in.md) | range | MaterialContainer |
| [MaterialSamplingProcess](MaterialSamplingProcess.md) | [collected_into](collected_into.md) | range | MaterialContainer |



## Identifier and Mapping Information







### Schema Source


* from schema: http://example.com/monet_schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['monet_schema:MaterialContainer'] |
| native | ['monet_schema:MaterialContainer'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaterialContainer
title: Material container
from_schema: http://example.com/monet_schema
rank: 1000
slots:
- container_size
- container_type

```
</details>

### Induced

<details>
```yaml
name: MaterialContainer
title: Material container
from_schema: http://example.com/monet_schema
rank: 1000
attributes:
  container_size:
    name: container_size
    title: container size
    from_schema: http://example.com/monet_schema
    rank: 1000
    alias: container_size
    owner: MaterialContainer
    domain_of:
    - MaterialContainer
    range: QuantityValue
    inlined: true
  container_type:
    name: container_type
    title: container type
    from_schema: http://example.com/monet_schema
    rank: 1000
    alias: container_type
    owner: MaterialContainer
    domain_of:
    - MaterialContainer
    range: ContainerTypeEnum

```
</details>