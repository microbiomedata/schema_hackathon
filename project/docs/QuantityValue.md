
# Class: QuantityValue




URI: [monet_schema:QuantityValue](http://example.com/monet_schema/QuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MatSampProc]++-%20amount%201..1>[QuantityValue&#124;has_value:float;has_unit:string],[Shaker]++-%20shake_speed%200..1>[QuantityValue],[Shaker]++-%20shake_time%200..1>[QuantityValue],[MaterialContainer]++-%20size%201..1>[QuantityValue],[Dissolving]++-%20volume%201..1>[QuantityValue],[Shaker],[MaterialContainer],[MatSampProc],[Dissolving])](https://yuml.me/diagram/nofunky;dir:TB/class/[MatSampProc]++-%20amount%201..1>[QuantityValue&#124;has_value:float;has_unit:string],[Shaker]++-%20shake_speed%200..1>[QuantityValue],[Shaker]++-%20shake_time%200..1>[QuantityValue],[MaterialContainer]++-%20size%201..1>[QuantityValue],[Dissolving]++-%20volume%201..1>[QuantityValue],[Shaker],[MaterialContainer],[MatSampProc],[Dissolving])

## Referenced by Class

 *  **None** *[amount](amount.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[shake_speed](shake_speed.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[shake_time](shake_time.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[size](size.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[volume](volume.md)*  <sub>1..1</sub>  **[QuantityValue](QuantityValue.md)**

## Attributes


### Own

 * [has_value](has_value.md)  <sub>1..1</sub>
     * Range: [Float](types/Float.md)
 * [has_unit](has_unit.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
