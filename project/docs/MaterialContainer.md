
# Class: MaterialContainer




URI: [monet_schema:MaterialContainer](http://example.com/monet_schema/MaterialContainer)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<container_size%200..1-++[MaterialContainer&#124;container_type:ContainerTypeEnum%20%3F],[MaterialSamplingProcess]++-%20collected_into%200..1>[MaterialContainer],[DissolvingProcess]++-%20dissolved_in%200..1>[MaterialContainer],[MaterialSamplingProcess],[DissolvingProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<container_size%200..1-++[MaterialContainer&#124;container_type:ContainerTypeEnum%20%3F],[MaterialSamplingProcess]++-%20collected_into%200..1>[MaterialContainer],[DissolvingProcess]++-%20dissolved_in%200..1>[MaterialContainer],[MaterialSamplingProcess],[DissolvingProcess])

## Referenced by Class

 *  **None** *[collected_into](collected_into.md)*  <sub>0..1</sub>  **[MaterialContainer](MaterialContainer.md)**
 *  **None** *[dissolved_in](dissolved_in.md)*  <sub>0..1</sub>  **[MaterialContainer](MaterialContainer.md)**

## Attributes


### Own

 * [container_size](container_size.md)  <sub>0..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [container_type](container_type.md)  <sub>0..1</sub>
     * Range: [ContainerTypeEnum](ContainerTypeEnum.md)
