# Auto generated from schema_hackathon.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-07T11:41:17
# Schema: monet_schema
#
# id: http://example.com/monet_schema
# description: A sandbox for modeling MONET sample processing activities
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MONET_DATA = CurieNamespace('monet_data', 'http://example.com/monet_data/')
MONET_SCHEMA = CurieNamespace('monet_schema', 'http://example.com/monet_schema/')
DEFAULT_ = MONET_SCHEMA


# Types

# Class references
class NamedThingId(extended_str):
    pass


class DatabaseId(NamedThingId):
    pass


class MaterialSampleId(NamedThingId):
    pass


@dataclass
class DissolvingProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002773"]
    class_class_curie: ClassVar[str] = "CHMO:0002773"
    class_name: ClassVar[str] = "DissolvingProcess"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.DissolvingProcess

    material_input: Optional[Union[str, MaterialSampleId]] = None
    material_output: Optional[Union[str, MaterialSampleId]] = None
    dissolution_aided_by: Optional[Union[dict, "LabDevice"]] = None
    dissolution_reagent: Optional[Union[str, "SolventEnum"]] = None
    dissolution_volume: Optional[Union[dict, "QuantityValue"]] = None
    dissolved_in: Optional[Union[dict, "MaterialContainer"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.material_input is not None and not isinstance(self.material_input, MaterialSampleId):
            self.material_input = MaterialSampleId(self.material_input)

        if self.material_output is not None and not isinstance(self.material_output, MaterialSampleId):
            self.material_output = MaterialSampleId(self.material_output)

        if self.dissolution_aided_by is not None and not isinstance(self.dissolution_aided_by, LabDevice):
            self.dissolution_aided_by = LabDevice(**as_dict(self.dissolution_aided_by))

        if self.dissolution_reagent is not None and not isinstance(self.dissolution_reagent, SolventEnum):
            self.dissolution_reagent = SolventEnum(self.dissolution_reagent)

        if self.dissolution_volume is not None and not isinstance(self.dissolution_volume, QuantityValue):
            self.dissolution_volume = QuantityValue(**as_dict(self.dissolution_volume))

        if self.dissolved_in is not None and not isinstance(self.dissolved_in, MaterialContainer):
            self.dissolved_in = MaterialContainer(**as_dict(self.dissolved_in))

        super().__post_init__(**kwargs)


@dataclass
class LabDevice(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.LabDevice
    class_class_curie: ClassVar[str] = "monet_schema:LabDevice"
    class_name: ClassVar[str] = "LabDevice"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.LabDevice

    device_type: Optional[Union[str, "DeviceTypeEnum"]] = None
    process_speed: Optional[Union[dict, "QuantityValue"]] = None
    process_temperature: Optional[Union[dict, "QuantityValue"]] = None
    process_time: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.device_type is not None and not isinstance(self.device_type, DeviceTypeEnum):
            self.device_type = DeviceTypeEnum(self.device_type)

        if self.process_speed is not None and not isinstance(self.process_speed, QuantityValue):
            self.process_speed = QuantityValue(**as_dict(self.process_speed))

        if self.process_temperature is not None and not isinstance(self.process_temperature, QuantityValue):
            self.process_temperature = QuantityValue(**as_dict(self.process_temperature))

        if self.process_time is not None and not isinstance(self.process_time, QuantityValue):
            self.process_time = QuantityValue(**as_dict(self.process_time))

        super().__post_init__(**kwargs)


@dataclass
class MaterialContainer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.MaterialContainer
    class_class_curie: ClassVar[str] = "monet_schema:MaterialContainer"
    class_name: ClassVar[str] = "MaterialContainer"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.MaterialContainer

    container_size: Optional[Union[dict, "QuantityValue"]] = None
    container_type: Optional[Union[str, "ContainerTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.container_size is not None and not isinstance(self.container_size, QuantityValue):
            self.container_size = QuantityValue(**as_dict(self.container_size))

        if self.container_type is not None and not isinstance(self.container_type, ContainerTypeEnum):
            self.container_type = ContainerTypeEnum(self.container_type)

        super().__post_init__(**kwargs)


@dataclass
class MaterialSamplingProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000744"]
    class_class_curie: ClassVar[str] = "OBI:0000744"
    class_name: ClassVar[str] = "MaterialSamplingProcess"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.MaterialSamplingProcess

    collected_into: Optional[Union[dict, MaterialContainer]] = None
    material_input: Optional[Union[str, MaterialSampleId]] = None
    material_output: Optional[Union[str, MaterialSampleId]] = None
    amount_collected: Optional[Union[dict, "QuantityValue"]] = None
    sampling_method: Optional[Union[str, "SamplingMethodEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.collected_into is not None and not isinstance(self.collected_into, MaterialContainer):
            self.collected_into = MaterialContainer(**as_dict(self.collected_into))

        if self.material_input is not None and not isinstance(self.material_input, MaterialSampleId):
            self.material_input = MaterialSampleId(self.material_input)

        if self.material_output is not None and not isinstance(self.material_output, MaterialSampleId):
            self.material_output = MaterialSampleId(self.material_output)

        if self.amount_collected is not None and not isinstance(self.amount_collected, QuantityValue):
            self.amount_collected = QuantityValue(**as_dict(self.amount_collected))

        if self.sampling_method is not None and not isinstance(self.sampling_method, SamplingMethodEnum):
            self.sampling_method = SamplingMethodEnum(self.sampling_method)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.NamedThing
    class_class_curie: ClassVar[str] = "monet_schema:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Database(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.Database
    class_class_curie: ClassVar[str] = "monet_schema:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.Database

    id: Union[str, DatabaseId] = None
    material_sample_set: Optional[Union[Dict[Union[str, MaterialSampleId], Union[dict, "MaterialSample"]], List[Union[dict, "MaterialSample"]]]] = empty_dict()
    dissolving_process_set: Optional[Union[Union[dict, "DissolvingProcess"], List[Union[dict, "DissolvingProcess"]]]] = empty_list()
    material_sampling_process_set: Optional[Union[Union[dict, "MaterialSamplingProcess"], List[Union[dict, "MaterialSamplingProcess"]]]] = empty_list()
    reaction_activity_set: Optional[Union[Union[dict, "ReactionActivity"], List[Union[dict, "ReactionActivity"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatabaseId):
            self.id = DatabaseId(self.id)

        self._normalize_inlined_as_list(slot_name="material_sample_set", slot_type=MaterialSample, key_name="id", keyed=True)

        if not isinstance(self.dissolving_process_set, list):
            self.dissolving_process_set = [self.dissolving_process_set] if self.dissolving_process_set is not None else []
        self.dissolving_process_set = [v if isinstance(v, DissolvingProcess) else DissolvingProcess(**as_dict(v)) for v in self.dissolving_process_set]

        if not isinstance(self.material_sampling_process_set, list):
            self.material_sampling_process_set = [self.material_sampling_process_set] if self.material_sampling_process_set is not None else []
        self.material_sampling_process_set = [v if isinstance(v, MaterialSamplingProcess) else MaterialSamplingProcess(**as_dict(v)) for v in self.material_sampling_process_set]

        if not isinstance(self.reaction_activity_set, list):
            self.reaction_activity_set = [self.reaction_activity_set] if self.reaction_activity_set is not None else []
        self.reaction_activity_set = [v if isinstance(v, ReactionActivity) else ReactionActivity(**as_dict(v)) for v in self.reaction_activity_set]

        super().__post_init__(**kwargs)


@dataclass
class MaterialSample(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.MaterialSample
    class_class_curie: ClassVar[str] = "monet_schema:MaterialSample"
    class_name: ClassVar[str] = "MaterialSample"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.MaterialSample

    id: Union[str, MaterialSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class QuantityValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.QuantityValue
    class_class_curie: ClassVar[str] = "monet_schema:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.QuantityValue

    has_value: Optional[float] = None
    has_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_value is not None and not isinstance(self.has_value, float):
            self.has_value = float(self.has_value)

        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        super().__post_init__(**kwargs)


@dataclass
class ReactionActivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.ReactionActivity
    class_class_curie: ClassVar[str] = "monet_schema:ReactionActivity"
    class_name: ClassVar[str] = "ReactionActivity"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.ReactionActivity

    material_input: Optional[Union[str, MaterialSampleId]] = None
    material_output: Optional[Union[str, MaterialSampleId]] = None
    reaction_time: Optional[Union[dict, QuantityValue]] = None
    reaction_aided_by: Optional[Union[dict, LabDevice]] = None
    reaction_temperature: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.material_input is not None and not isinstance(self.material_input, MaterialSampleId):
            self.material_input = MaterialSampleId(self.material_input)

        if self.material_output is not None and not isinstance(self.material_output, MaterialSampleId):
            self.material_output = MaterialSampleId(self.material_output)

        if self.reaction_time is not None and not isinstance(self.reaction_time, QuantityValue):
            self.reaction_time = QuantityValue(**as_dict(self.reaction_time))

        if self.reaction_aided_by is not None and not isinstance(self.reaction_aided_by, LabDevice):
            self.reaction_aided_by = LabDevice(**as_dict(self.reaction_aided_by))

        if self.reaction_temperature is not None and not isinstance(self.reaction_temperature, str):
            self.reaction_temperature = str(self.reaction_temperature)

        super().__post_init__(**kwargs)


# Enumerations
class ContainerTypeEnum(EnumDefinitionImpl):

    screw_top_conical = PermissibleValue(text="screw_top_conical")

    _defn = EnumDefinition(
        name="ContainerTypeEnum",
    )

class DeviceTypeEnum(EnumDefinitionImpl):

    orbital_shaker = PermissibleValue(text="orbital_shaker")
    thermomixer = PermissibleValue(text="thermomixer")

    _defn = EnumDefinition(
        name="DeviceTypeEnum",
    )

class SamplingMethodEnum(EnumDefinitionImpl):

    weighing = PermissibleValue(text="weighing")

    _defn = EnumDefinition(
        name="SamplingMethodEnum",
    )

class SolventEnum(EnumDefinitionImpl):

    deionized_water = PermissibleValue(text="deionized_water")

    _defn = EnumDefinition(
        name="SolventEnum",
    )

# Slots
class slots:
    pass

slots.material_sample_set = Slot(uri=MONET_SCHEMA.material_sample_set, name="material_sample_set", curie=MONET_SCHEMA.curie('material_sample_set'),
                   model_uri=MONET_SCHEMA.material_sample_set, domain=None, range=Optional[Union[Dict[Union[str, MaterialSampleId], Union[dict, MaterialSample]], List[Union[dict, MaterialSample]]]])

slots.dissolving_process_set = Slot(uri=MONET_SCHEMA.dissolving_process_set, name="dissolving_process_set", curie=MONET_SCHEMA.curie('dissolving_process_set'),
                   model_uri=MONET_SCHEMA.dissolving_process_set, domain=None, range=Optional[Union[Union[dict, DissolvingProcess], List[Union[dict, DissolvingProcess]]]])

slots.material_sampling_process_set = Slot(uri=MONET_SCHEMA.material_sampling_process_set, name="material_sampling_process_set", curie=MONET_SCHEMA.curie('material_sampling_process_set'),
                   model_uri=MONET_SCHEMA.material_sampling_process_set, domain=None, range=Optional[Union[Union[dict, MaterialSamplingProcess], List[Union[dict, MaterialSamplingProcess]]]])

slots.reaction_activity_set = Slot(uri=MONET_SCHEMA.reaction_activity_set, name="reaction_activity_set", curie=MONET_SCHEMA.curie('reaction_activity_set'),
                   model_uri=MONET_SCHEMA.reaction_activity_set, domain=None, range=Optional[Union[Union[dict, ReactionActivity], List[Union[dict, ReactionActivity]]]])

slots.material_input = Slot(uri=MONET_SCHEMA.material_input, name="material_input", curie=MONET_SCHEMA.curie('material_input'),
                   model_uri=MONET_SCHEMA.material_input, domain=None, range=Optional[Union[str, MaterialSampleId]])

slots.material_output = Slot(uri=MONET_SCHEMA.material_output, name="material_output", curie=MONET_SCHEMA.curie('material_output'),
                   model_uri=MONET_SCHEMA.material_output, domain=None, range=Optional[Union[str, MaterialSampleId]])

slots.dissolution_aided_by = Slot(uri=MONET_SCHEMA.dissolution_aided_by, name="dissolution_aided_by", curie=MONET_SCHEMA.curie('dissolution_aided_by'),
                   model_uri=MONET_SCHEMA.dissolution_aided_by, domain=None, range=Optional[Union[dict, LabDevice]])

slots.dissolution_reagent = Slot(uri=MONET_SCHEMA.dissolution_reagent, name="dissolution_reagent", curie=MONET_SCHEMA.curie('dissolution_reagent'),
                   model_uri=MONET_SCHEMA.dissolution_reagent, domain=None, range=Optional[Union[str, "SolventEnum"]])

slots.dissolution_volume = Slot(uri=MONET_SCHEMA.dissolution_volume, name="dissolution_volume", curie=MONET_SCHEMA.curie('dissolution_volume'),
                   model_uri=MONET_SCHEMA.dissolution_volume, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dissolved_in = Slot(uri=MONET_SCHEMA.dissolved_in, name="dissolved_in", curie=MONET_SCHEMA.curie('dissolved_in'),
                   model_uri=MONET_SCHEMA.dissolved_in, domain=None, range=Optional[Union[dict, MaterialContainer]])

slots.device_type = Slot(uri=MONET_SCHEMA.device_type, name="device_type", curie=MONET_SCHEMA.curie('device_type'),
                   model_uri=MONET_SCHEMA.device_type, domain=None, range=Optional[Union[str, "DeviceTypeEnum"]])

slots.process_speed = Slot(uri=MONET_SCHEMA.process_speed, name="process_speed", curie=MONET_SCHEMA.curie('process_speed'),
                   model_uri=MONET_SCHEMA.process_speed, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.process_temperature = Slot(uri=MONET_SCHEMA.process_temperature, name="process_temperature", curie=MONET_SCHEMA.curie('process_temperature'),
                   model_uri=MONET_SCHEMA.process_temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.process_time = Slot(uri=MONET_SCHEMA.process_time, name="process_time", curie=MONET_SCHEMA.curie('process_time'),
                   model_uri=MONET_SCHEMA.process_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.container_size = Slot(uri=MONET_SCHEMA.container_size, name="container_size", curie=MONET_SCHEMA.curie('container_size'),
                   model_uri=MONET_SCHEMA.container_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.container_type = Slot(uri=MONET_SCHEMA.container_type, name="container_type", curie=MONET_SCHEMA.curie('container_type'),
                   model_uri=MONET_SCHEMA.container_type, domain=None, range=Optional[Union[str, "ContainerTypeEnum"]])

slots.collected_into = Slot(uri=MONET_SCHEMA.collected_into, name="collected_into", curie=MONET_SCHEMA.curie('collected_into'),
                   model_uri=MONET_SCHEMA.collected_into, domain=None, range=Optional[Union[dict, MaterialContainer]])

slots.amount_collected = Slot(uri=MONET_SCHEMA.amount_collected, name="amount_collected", curie=MONET_SCHEMA.curie('amount_collected'),
                   model_uri=MONET_SCHEMA.amount_collected, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sampling_method = Slot(uri=MONET_SCHEMA.sampling_method, name="sampling_method", curie=MONET_SCHEMA.curie('sampling_method'),
                   model_uri=MONET_SCHEMA.sampling_method, domain=None, range=Optional[Union[str, "SamplingMethodEnum"]])

slots.description = Slot(uri=MONET_SCHEMA.description, name="description", curie=MONET_SCHEMA.curie('description'),
                   model_uri=MONET_SCHEMA.description, domain=None, range=Optional[str])

slots.id = Slot(uri=MONET_SCHEMA.id, name="id", curie=MONET_SCHEMA.curie('id'),
                   model_uri=MONET_SCHEMA.id, domain=None, range=URIRef)

slots.has_value = Slot(uri=MONET_SCHEMA.has_value, name="has_value", curie=MONET_SCHEMA.curie('has_value'),
                   model_uri=MONET_SCHEMA.has_value, domain=None, range=Optional[float])

slots.has_unit = Slot(uri=MONET_SCHEMA.has_unit, name="has_unit", curie=MONET_SCHEMA.curie('has_unit'),
                   model_uri=MONET_SCHEMA.has_unit, domain=None, range=Optional[str])

slots.reaction_time = Slot(uri=MONET_SCHEMA.reaction_time, name="reaction_time", curie=MONET_SCHEMA.curie('reaction_time'),
                   model_uri=MONET_SCHEMA.reaction_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.reaction_aided_by = Slot(uri=MONET_SCHEMA.reaction_aided_by, name="reaction_aided_by", curie=MONET_SCHEMA.curie('reaction_aided_by'),
                   model_uri=MONET_SCHEMA.reaction_aided_by, domain=None, range=Optional[Union[dict, LabDevice]])

slots.reaction_temperature = Slot(uri=MONET_SCHEMA.reaction_temperature, name="reaction_temperature", curie=MONET_SCHEMA.curie('reaction_temperature'),
                   model_uri=MONET_SCHEMA.reaction_temperature, domain=None, range=Optional[str])