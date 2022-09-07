
# Class: Database




URI: [monet_schema:Database](http://example.com/monet_schema/Database)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ReactionActivity],[NamedThing],[MaterialSamplingProcess],[MaterialSample],[DissolvingProcess],[ReactionActivity]<reaction_activity_set%200..*-++[Database&#124;description(i):string%20%3F;id(i):string],[MaterialSamplingProcess]<material_sampling_process_set%200..*-++[Database],[MaterialSample]<material_sample_set%200..*-++[Database],[DissolvingProcess]<dissolving_process_set%200..*-++[Database],[NamedThing]^-[Database])](https://yuml.me/diagram/nofunky;dir:TB/class/[ReactionActivity],[NamedThing],[MaterialSamplingProcess],[MaterialSample],[DissolvingProcess],[ReactionActivity]<reaction_activity_set%200..*-++[Database&#124;description(i):string%20%3F;id(i):string],[MaterialSamplingProcess]<material_sampling_process_set%200..*-++[Database],[MaterialSample]<material_sample_set%200..*-++[Database],[DissolvingProcess]<dissolving_process_set%200..*-++[Database],[NamedThing]^-[Database])

## Parents

 *  is_a: [NamedThing](NamedThing.md)

## Attributes


### Own

 * [dissolving_process_set](dissolving_process_set.md)  <sub>0..\*</sub>
     * Range: [DissolvingProcess](DissolvingProcess.md)
 * [material_sample_set](material_sample_set.md)  <sub>0..\*</sub>
     * Range: [MaterialSample](MaterialSample.md)
 * [material_sampling_process_set](material_sampling_process_set.md)  <sub>0..\*</sub>
     * Range: [MaterialSamplingProcess](MaterialSamplingProcess.md)
 * [reaction_activity_set](reaction_activity_set.md)  <sub>0..\*</sub>
     * Range: [ReactionActivity](ReactionActivity.md)

### Inherited from NamedThing:

 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
