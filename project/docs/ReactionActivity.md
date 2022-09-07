
# Class: ReactionActivity




URI: [monet_schema:ReactionActivity](http://example.com/monet_schema/ReactionActivity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[LabDevice]<reaction_aided_by%200..1-++[ReactionActivity&#124;reaction_temperature:string%20%3F],[QuantityValue]<reaction_time%200..1-++[ReactionActivity],[MaterialSample]<material_output%200..1-%20[ReactionActivity],[MaterialSample]<material_input%200..1-%20[ReactionActivity],[Database]++-%20reaction_activity_set%200..*>[ReactionActivity],[QuantityValue],[MaterialSample],[LabDevice],[Database])](https://yuml.me/diagram/nofunky;dir:TB/class/[LabDevice]<reaction_aided_by%200..1-++[ReactionActivity&#124;reaction_temperature:string%20%3F],[QuantityValue]<reaction_time%200..1-++[ReactionActivity],[MaterialSample]<material_output%200..1-%20[ReactionActivity],[MaterialSample]<material_input%200..1-%20[ReactionActivity],[Database]++-%20reaction_activity_set%200..*>[ReactionActivity],[QuantityValue],[MaterialSample],[LabDevice],[Database])

## Referenced by Class

 *  **None** *[reaction_activity_set](reaction_activity_set.md)*  <sub>0..\*</sub>  **[ReactionActivity](ReactionActivity.md)**

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
 * [reaction_time](reaction_time.md)  <sub>0..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [reaction_aided_by](reaction_aided_by.md)  <sub>0..1</sub>
     * Range: [LabDevice](LabDevice.md)
 * [reaction_temperature](reaction_temperature.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | reaction-activity |

