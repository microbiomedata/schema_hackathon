
# Class: MaterialSamplingProcess




URI: [monet_schema:MaterialSamplingProcess](http://example.com/monet_schema/MaterialSamplingProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[MaterialSample]<material_output%200..1-%20[MaterialSamplingProcess&#124;sampling_method:SamplingMethodEnum%20%3F],[MaterialSample]<material_input%200..1-%20[MaterialSamplingProcess],[MaterialContainer]<collected_into%200..1-++[MaterialSamplingProcess],[QuantityValue]<amount_collected%200..1-++[MaterialSamplingProcess],[Database]++-%20material_sampling_process_set%200..*>[MaterialSamplingProcess],[MaterialSample],[MaterialContainer],[Database])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[MaterialSample]<material_output%200..1-%20[MaterialSamplingProcess&#124;sampling_method:SamplingMethodEnum%20%3F],[MaterialSample]<material_input%200..1-%20[MaterialSamplingProcess],[MaterialContainer]<collected_into%200..1-++[MaterialSamplingProcess],[QuantityValue]<amount_collected%200..1-++[MaterialSamplingProcess],[Database]++-%20material_sampling_process_set%200..*>[MaterialSamplingProcess],[MaterialSample],[MaterialContainer],[Database])

## Referenced by Class

 *  **None** *[material_sampling_process_set](material_sampling_process_set.md)*  <sub>0..\*</sub>  **[MaterialSamplingProcess](MaterialSamplingProcess.md)**

## Attributes


### Own

 * [amount_collected](amount_collected.md)  <sub>0..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [collected_into](collected_into.md)  <sub>0..1</sub>
     * Range: [MaterialContainer](MaterialContainer.md)
 * [material_input](material_input.md)  <sub>0..1</sub>
     * Range: [MaterialSample](MaterialSample.md)
     * Example: somextract:6 None
     * Example: soil:1 None
 * [material_output](material_output.md)  <sub>0..1</sub>
     * Range: [MaterialSample](MaterialSample.md)
     * Example: somextract:7 None
     * Example: somextract:6 None
 * [sampling_method](sampling_method.md)  <sub>0..1</sub>
     * Range: [SamplingMethodEnum](SamplingMethodEnum.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | weighing-activity |
| **Mappings:** | | OBI:0000744 |

