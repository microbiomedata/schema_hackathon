# Auto generated from schema_hackathon.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-29T18:40:15
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
MONET_SCHEMA = CurieNamespace('monet_schema', 'http://example.com/monet_schema/')
DEFAULT_ = MONET_SCHEMA


# Types

# Class references
class NamedThingId(extended_str):
    pass


class MaterialEntityId(NamedThingId):
    pass


@dataclass
class QuantityValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.QuantityValue
    class_class_curie: ClassVar[str] = "monet_schema:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.QuantityValue

    has_value: float = None
    has_unit: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.has_value):
            self.MissingRequiredField("has_value")
        if not isinstance(self.has_value, float):
            self.has_value = float(self.has_value)

        if self._is_empty(self.has_unit):
            self.MissingRequiredField("has_unit")
        if not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        super().__post_init__(**kwargs)


@dataclass
class MatSampProc(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000744"]
    class_class_curie: ClassVar[str] = "OBI:0000744"
    class_name: ClassVar[str] = "MatSampProc"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.MatSampProc

    collected_into: Union[dict, "MaterialContainer"] = None
    material_input: Union[dict, "NamedThing"] = None
    material_output: Union[dict, "NamedThing"] = None
    amount: Union[dict, QuantityValue] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.collected_into):
            self.MissingRequiredField("collected_into")
        if not isinstance(self.collected_into, MaterialContainer):
            self.collected_into = MaterialContainer(**as_dict(self.collected_into))

        if self._is_empty(self.material_input):
            self.MissingRequiredField("material_input")
        if not isinstance(self.material_input, NamedThing):
            self.material_input = NamedThing(**as_dict(self.material_input))

        if self._is_empty(self.material_output):
            self.MissingRequiredField("material_output")
        if not isinstance(self.material_output, NamedThing):
            self.material_output = NamedThing(**as_dict(self.material_output))

        if self._is_empty(self.amount):
            self.MissingRequiredField("amount")
        if not isinstance(self.amount, QuantityValue):
            self.amount = QuantityValue(**as_dict(self.amount))

        super().__post_init__(**kwargs)


@dataclass
class Dissolving(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002773"]
    class_class_curie: ClassVar[str] = "CHMO:0002773"
    class_name: ClassVar[str] = "Dissolving"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.Dissolving

    material_input: Union[dict, "NamedThing"] = None
    material_output: Union[dict, "NamedThing"] = None
    container: Union[dict, "MaterialContainer"] = None
    shaker_selection: Union[dict, "Shaker"] = None
    solvent: Union[str, "SolventEnum"] = None
    volume: Union[dict, QuantityValue] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.material_input):
            self.MissingRequiredField("material_input")
        if not isinstance(self.material_input, NamedThing):
            self.material_input = NamedThing(**as_dict(self.material_input))

        if self._is_empty(self.material_output):
            self.MissingRequiredField("material_output")
        if not isinstance(self.material_output, NamedThing):
            self.material_output = NamedThing(**as_dict(self.material_output))

        if self._is_empty(self.container):
            self.MissingRequiredField("container")
        if not isinstance(self.container, MaterialContainer):
            self.container = MaterialContainer(**as_dict(self.container))

        if self._is_empty(self.shaker_selection):
            self.MissingRequiredField("shaker_selection")
        if not isinstance(self.shaker_selection, Shaker):
            self.shaker_selection = Shaker(**as_dict(self.shaker_selection))

        if self._is_empty(self.solvent):
            self.MissingRequiredField("solvent")
        if not isinstance(self.solvent, SolventEnum):
            self.solvent = SolventEnum(self.solvent)

        if self._is_empty(self.volume):
            self.MissingRequiredField("volume")
        if not isinstance(self.volume, QuantityValue):
            self.volume = QuantityValue(**as_dict(self.volume))

        super().__post_init__(**kwargs)


@dataclass
class MaterialContainer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.MaterialContainer
    class_class_curie: ClassVar[str] = "monet_schema:MaterialContainer"
    class_name: ClassVar[str] = "MaterialContainer"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.MaterialContainer

    container_type: Union[str, "ContainerTypeEnum"] = None
    size: Union[dict, QuantityValue] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.container_type):
            self.MissingRequiredField("container_type")
        if not isinstance(self.container_type, ContainerTypeEnum):
            self.container_type = ContainerTypeEnum(self.container_type)

        if self._is_empty(self.size):
            self.MissingRequiredField("size")
        if not isinstance(self.size, QuantityValue):
            self.size = QuantityValue(**as_dict(self.size))

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.NamedThing
    class_class_curie: ClassVar[str] = "monet_schema:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Shaker(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.Shaker
    class_class_curie: ClassVar[str] = "monet_schema:Shaker"
    class_name: ClassVar[str] = "Shaker"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.Shaker

    shake_speed: Optional[Union[dict, QuantityValue]] = None
    shake_time: Optional[Union[dict, QuantityValue]] = None
    shaker_type: Optional[Union[str, "ShakerTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.shake_speed is not None and not isinstance(self.shake_speed, QuantityValue):
            self.shake_speed = QuantityValue(**as_dict(self.shake_speed))

        if self.shake_time is not None and not isinstance(self.shake_time, QuantityValue):
            self.shake_time = QuantityValue(**as_dict(self.shake_time))

        if self.shaker_type is not None and not isinstance(self.shaker_type, ShakerTypeEnum):
            self.shaker_type = ShakerTypeEnum(self.shaker_type)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONET_SCHEMA.MaterialEntity
    class_class_curie: ClassVar[str] = "monet_schema:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = MONET_SCHEMA.MaterialEntity

    id: Union[str, MaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class SolventEnum(EnumDefinitionImpl):

    deionized_water = PermissibleValue(text="deionized_water")

    _defn = EnumDefinition(
        name="SolventEnum",
    )

class ContainerTypeEnum(EnumDefinitionImpl):

    screw_top_conical = PermissibleValue(text="screw_top_conical")

    _defn = EnumDefinition(
        name="ContainerTypeEnum",
    )

class ShakerTypeEnum(EnumDefinitionImpl):

    orbital = PermissibleValue(text="orbital")

    _defn = EnumDefinition(
        name="ShakerTypeEnum",
    )

# Slots
class slots:
    pass

slots.container_type = Slot(uri=MONET_SCHEMA.container_type, name="container_type", curie=MONET_SCHEMA.curie('container_type'),
                   model_uri=MONET_SCHEMA.container_type, domain=None, range=Union[str, "ContainerTypeEnum"])

slots.has_value = Slot(uri=MONET_SCHEMA.has_value, name="has_value", curie=MONET_SCHEMA.curie('has_value'),
                   model_uri=MONET_SCHEMA.has_value, domain=None, range=float)

slots.collected_into = Slot(uri=MONET_SCHEMA.collected_into, name="collected_into", curie=MONET_SCHEMA.curie('collected_into'),
                   model_uri=MONET_SCHEMA.collected_into, domain=None, range=Union[dict, MaterialContainer])

slots.container = Slot(uri=MONET_SCHEMA.container, name="container", curie=MONET_SCHEMA.curie('container'),
                   model_uri=MONET_SCHEMA.container, domain=None, range=Union[dict, MaterialContainer])

slots.material_input = Slot(uri=MONET_SCHEMA.material_input, name="material_input", curie=MONET_SCHEMA.curie('material_input'),
                   model_uri=MONET_SCHEMA.material_input, domain=None, range=Union[dict, NamedThing])

slots.material_output = Slot(uri=MONET_SCHEMA.material_output, name="material_output", curie=MONET_SCHEMA.curie('material_output'),
                   model_uri=MONET_SCHEMA.material_output, domain=None, range=Union[dict, NamedThing])

slots.amount = Slot(uri=MONET_SCHEMA.amount, name="amount", curie=MONET_SCHEMA.curie('amount'),
                   model_uri=MONET_SCHEMA.amount, domain=None, range=Union[dict, QuantityValue])

slots.shake_speed = Slot(uri=MONET_SCHEMA.shake_speed, name="shake_speed", curie=MONET_SCHEMA.curie('shake_speed'),
                   model_uri=MONET_SCHEMA.shake_speed, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.shake_time = Slot(uri=MONET_SCHEMA.shake_time, name="shake_time", curie=MONET_SCHEMA.curie('shake_time'),
                   model_uri=MONET_SCHEMA.shake_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.size = Slot(uri=MONET_SCHEMA.size, name="size", curie=MONET_SCHEMA.curie('size'),
                   model_uri=MONET_SCHEMA.size, domain=None, range=Union[dict, QuantityValue])

slots.volume = Slot(uri=MONET_SCHEMA.volume, name="volume", curie=MONET_SCHEMA.curie('volume'),
                   model_uri=MONET_SCHEMA.volume, domain=None, range=Union[dict, QuantityValue])

slots.shaker_selection = Slot(uri=MONET_SCHEMA.shaker_selection, name="shaker_selection", curie=MONET_SCHEMA.curie('shaker_selection'),
                   model_uri=MONET_SCHEMA.shaker_selection, domain=None, range=Union[dict, Shaker])

slots.solvent = Slot(uri=MONET_SCHEMA.solvent, name="solvent", curie=MONET_SCHEMA.curie('solvent'),
                   model_uri=MONET_SCHEMA.solvent, domain=None, range=Union[str, "SolventEnum"])

slots.has_unit = Slot(uri=MONET_SCHEMA.has_unit, name="has_unit", curie=MONET_SCHEMA.curie('has_unit'),
                   model_uri=MONET_SCHEMA.has_unit, domain=None, range=str)

slots.shaker_type = Slot(uri=MONET_SCHEMA.shaker_type, name="shaker_type", curie=MONET_SCHEMA.curie('shaker_type'),
                   model_uri=MONET_SCHEMA.shaker_type, domain=None, range=Optional[Union[str, "ShakerTypeEnum"]])

slots.id = Slot(uri=MONET_SCHEMA.id, name="id", curie=MONET_SCHEMA.curie('id'),
                   model_uri=MONET_SCHEMA.id, domain=None, range=URIRef)