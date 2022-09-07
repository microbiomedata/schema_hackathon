
# Class: LabDevice




URI: [monet_schema:LabDevice](http://example.com/monet_schema/LabDevice)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<process_time%200..1-++[LabDevice&#124;device_type:DeviceTypeEnum%20%3F],[QuantityValue]<process_temperature%200..1-++[LabDevice],[QuantityValue]<process_speed%200..1-++[LabDevice],[DissolvingProcess]++-%20dissolution_aided_by%200..1>[LabDevice],[ReactionActivity]++-%20reaction_aided_by%200..1>[LabDevice],[ReactionActivity],[DissolvingProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<process_time%200..1-++[LabDevice&#124;device_type:DeviceTypeEnum%20%3F],[QuantityValue]<process_temperature%200..1-++[LabDevice],[QuantityValue]<process_speed%200..1-++[LabDevice],[DissolvingProcess]++-%20dissolution_aided_by%200..1>[LabDevice],[ReactionActivity]++-%20reaction_aided_by%200..1>[LabDevice],[ReactionActivity],[DissolvingProcess])

## Referenced by Class

 *  **None** *[dissolution_aided_by](dissolution_aided_by.md)*  <sub>0..1</sub>  **[LabDevice](LabDevice.md)**
 *  **None** *[reaction_aided_by](reaction_aided_by.md)*  <sub>0..1</sub>  **[LabDevice](LabDevice.md)**

## Attributes


### Own

 * [device_type](device_type.md)  <sub>0..1</sub>
     * Range: [DeviceTypeEnum](DeviceTypeEnum.md)
 * [process_speed](process_speed.md)  <sub>0..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [process_temperature](process_temperature.md)  <sub>0..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [process_time](process_time.md)  <sub>0..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
