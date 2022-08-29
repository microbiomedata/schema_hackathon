
# Class: Dissolving




URI: [monet_schema:Dissolving](http://example.com/monet_schema/Dissolving)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Shaker],[QuantityValue],[NamedThing],[MaterialContainer],[QuantityValue]<volume%201..1-++[Dissolving&#124;solvent:SolventEnum],[Shaker]<shaker_selection%201..1-++[Dissolving],[MaterialContainer]<container%201..1-++[Dissolving],[NamedThing]<material_output%201..1-++[Dissolving],[NamedThing]<material_input%201..1-++[Dissolving])](https://yuml.me/diagram/nofunky;dir:TB/class/[Shaker],[QuantityValue],[NamedThing],[MaterialContainer],[QuantityValue]<volume%201..1-++[Dissolving&#124;solvent:SolventEnum],[Shaker]<shaker_selection%201..1-++[Dissolving],[MaterialContainer]<container%201..1-++[Dissolving],[NamedThing]<material_output%201..1-++[Dissolving],[NamedThing]<material_input%201..1-++[Dissolving])

## Attributes


### Own

 * [material_input](material_input.md)  <sub>1..1</sub>
     * Range: [NamedThing](NamedThing.md)
     * Example: somextract:6 None
     * Example: soil:1 None
 * [material_output](material_output.md)  <sub>1..1</sub>
     * Range: [NamedThing](NamedThing.md)
     * Example: somextract:7 None
     * Example: somextract:6 None
 * [container](container.md)  <sub>1..1</sub>
     * Range: [MaterialContainer](MaterialContainer.md)
 * [shaker_selection](shaker_selection.md)  <sub>1..1</sub>
     * Range: [Shaker](Shaker.md)
 * [solvent](solvent.md)  <sub>1..1</sub>
     * Range: [SolventEnum](SolventEnum.md)
 * [volume](volume.md)  <sub>1..1</sub>
     * Range: [QuantityValue](QuantityValue.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | dissolution-activity |
| **Mappings:** | | CHMO:0002773 |

