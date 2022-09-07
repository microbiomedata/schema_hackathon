
# Class: MaterialSample




URI: [monet_schema:MaterialSample](http://example.com/monet_schema/MaterialSample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DissolvingProcess]-%20material_input%200..1>[MaterialSample&#124;description(i):string%20%3F;id(i):string],[MaterialSamplingProcess]-%20material_input%200..1>[MaterialSample],[ReactionActivity]-%20material_input%200..1>[MaterialSample],[DissolvingProcess]-%20material_output%200..1>[MaterialSample],[MaterialSamplingProcess]-%20material_output%200..1>[MaterialSample],[ReactionActivity]-%20material_output%200..1>[MaterialSample],[Database]++-%20material_sample_set%200..*>[MaterialSample],[NamedThing]^-[MaterialSample],[ReactionActivity],[MaterialSamplingProcess],[DissolvingProcess],[Database])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DissolvingProcess]-%20material_input%200..1>[MaterialSample&#124;description(i):string%20%3F;id(i):string],[MaterialSamplingProcess]-%20material_input%200..1>[MaterialSample],[ReactionActivity]-%20material_input%200..1>[MaterialSample],[DissolvingProcess]-%20material_output%200..1>[MaterialSample],[MaterialSamplingProcess]-%20material_output%200..1>[MaterialSample],[ReactionActivity]-%20material_output%200..1>[MaterialSample],[Database]++-%20material_sample_set%200..*>[MaterialSample],[NamedThing]^-[MaterialSample],[ReactionActivity],[MaterialSamplingProcess],[DissolvingProcess],[Database])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Referenced by Class

 *  **None** *[material_input](material_input.md)*  <sub>0..1</sub>  **[MaterialSample](MaterialSample.md)**
 *  **None** *[material_output](material_output.md)*  <sub>0..1</sub>  **[MaterialSample](MaterialSample.md)**
 *  **None** *[material_sample_set](material_sample_set.md)*  <sub>0..\*</sub>  **[MaterialSample](MaterialSample.md)**

## Attributes


### Inherited from NamedThing:

 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Material entity |

