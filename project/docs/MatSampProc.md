
# Class: MatSampProc




URI: [monet_schema:MatSampProc](http://example.com/monet_schema/MatSampProc)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[NamedThing],[MaterialContainer],[NamedThing]<material_output%201..1-++[MatSampProc],[NamedThing]<material_input%201..1-++[MatSampProc],[MaterialContainer]<collected_into%201..1-++[MatSampProc],[QuantityValue]<amount%201..1-++[MatSampProc])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[NamedThing],[MaterialContainer],[NamedThing]<material_output%201..1-++[MatSampProc],[NamedThing]<material_input%201..1-++[MatSampProc],[MaterialContainer]<collected_into%201..1-++[MatSampProc],[QuantityValue]<amount%201..1-++[MatSampProc])

## Attributes


### Own

 * [amount](amount.md)  <sub>1..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [collected_into](collected_into.md)  <sub>1..1</sub>
     * Range: [MaterialContainer](MaterialContainer.md)
 * [material_input](material_input.md)  <sub>1..1</sub>
     * Range: [NamedThing](NamedThing.md)
     * Example: soil:1 None
 * [material_output](material_output.md)  <sub>1..1</sub>
     * Range: [NamedThing](NamedThing.md)
     * Example: somextract:6 None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | weighing-activity |
| **Mappings:** | | OBI:0000744 |

