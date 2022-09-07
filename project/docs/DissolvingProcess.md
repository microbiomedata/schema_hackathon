
# Class: DissolvingProcess




URI: [monet_schema:DissolvingProcess](http://example.com/monet_schema/DissolvingProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[MaterialSample],[MaterialContainer],[LabDevice],[MaterialContainer]<dissolved_in%200..1-++[DissolvingProcess&#124;dissolution_reagent:SolventEnum%20%3F],[QuantityValue]<dissolution_volume%200..1-++[DissolvingProcess],[LabDevice]<dissolution_aided_by%200..1-++[DissolvingProcess],[MaterialSample]<material_output%200..1-%20[DissolvingProcess],[MaterialSample]<material_input%200..1-%20[DissolvingProcess],[Database]++-%20dissolving_process_set%200..*>[DissolvingProcess],[Database])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[MaterialSample],[MaterialContainer],[LabDevice],[MaterialContainer]<dissolved_in%200..1-++[DissolvingProcess&#124;dissolution_reagent:SolventEnum%20%3F],[QuantityValue]<dissolution_volume%200..1-++[DissolvingProcess],[LabDevice]<dissolution_aided_by%200..1-++[DissolvingProcess],[MaterialSample]<material_output%200..1-%20[DissolvingProcess],[MaterialSample]<material_input%200..1-%20[DissolvingProcess],[Database]++-%20dissolving_process_set%200..*>[DissolvingProcess],[Database])

## Referenced by Class

 *  **None** *[dissolving_process_set](dissolving_process_set.md)*  <sub>0..\*</sub>  **[DissolvingProcess](DissolvingProcess.md)**

## Attributes


### Own

 * [material_input](material_input.md)  <sub>0..1</sub>
     * Range: [MaterialSample](MaterialSample.md)
     * Example: somextract:6 None
     * Example: soil:1 None
 * [material_output](material_output.md)  <sub>0..1</sub>
     * Range: [MaterialSample](MaterialSample.md)
     * Example: somextract:7 None
     * Example: somextract:6 None
 * [dissolution_aided_by](dissolution_aided_by.md)  <sub>0..1</sub>
     * Range: [LabDevice](LabDevice.md)
 * [dissolution_reagent](dissolution_reagent.md)  <sub>0..1</sub>
     * Range: [SolventEnum](SolventEnum.md)
 * [dissolution_volume](dissolution_volume.md)  <sub>0..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [dissolved_in](dissolved_in.md)  <sub>0..1</sub>
     * Range: [MaterialContainer](MaterialContainer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | dissolution-activity |
| **Mappings:** | | CHMO:0002773 |

