
# Class: Shaker




URI: [monet_schema:Shaker](http://example.com/monet_schema/Shaker)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<shake_time%200..1-++[Shaker&#124;shaker_type:ShakerTypeEnum%20%3F],[QuantityValue]<shake_speed%200..1-++[Shaker],[Dissolving]++-%20shaker_selection%201..1>[Shaker],[QuantityValue],[Dissolving])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<shake_time%200..1-++[Shaker&#124;shaker_type:ShakerTypeEnum%20%3F],[QuantityValue]<shake_speed%200..1-++[Shaker],[Dissolving]++-%20shaker_selection%201..1>[Shaker],[QuantityValue],[Dissolving])

## Referenced by Class

 *  **None** *[shaker_selection](shaker_selection.md)*  <sub>1..1</sub>  **[Shaker](Shaker.md)**

## Attributes


### Own

 * [shake_speed](shake_speed.md)  <sub>0..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [shake_time](shake_time.md)  <sub>0..1</sub>
     * Range: [QuantityValue](QuantityValue.md)
 * [shaker_type](shaker_type.md)  <sub>0..1</sub>
     * Range: [ShakerTypeEnum](ShakerTypeEnum.md)
