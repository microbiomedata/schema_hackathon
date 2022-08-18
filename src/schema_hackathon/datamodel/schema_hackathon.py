# Auto generated from schema_hackathon.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-16T10:52:27
# Schema: nmdc_hackathon_schema
#
# id: http://example.com/hackschema
# description: A sandbox for NMDC team members to hack the schema
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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
HACKSCHEMA = CurieNamespace('hackschema', 'http://example.com/hackschema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = HACKSCHEMA


# Types

# Class references



@dataclass
class Mammal(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HACKSCHEMA.Mammal
    class_class_curie: ClassVar[str] = "hackschema:Mammal"
    class_name: ClassVar[str] = "Mammal"
    class_model_uri: ClassVar[URIRef] = HACKSCHEMA.Mammal

    eye_color: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.eye_color is not None and not isinstance(self.eye_color, str):
            self.eye_color = str(self.eye_color)

        super().__post_init__(**kwargs)


@dataclass
class Human(Mammal):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HACKSCHEMA.Human
    class_class_curie: ClassVar[str] = "hackschema:Human"
    class_name: ClassVar[str] = "Human"
    class_model_uri: ClassVar[URIRef] = HACKSCHEMA.Human

    human_full_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.human_full_name is not None and not isinstance(self.human_full_name, str):
            self.human_full_name = str(self.human_full_name)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.human_full_name = Slot(uri=HACKSCHEMA.human_full_name, name="human_full_name", curie=HACKSCHEMA.curie('human_full_name'),
                   model_uri=HACKSCHEMA.human_full_name, domain=None, range=Optional[str])

slots.eye_color = Slot(uri=HACKSCHEMA.eye_color, name="eye_color", curie=HACKSCHEMA.curie('eye_color'),
                   model_uri=HACKSCHEMA.eye_color, domain=None, range=Optional[str])

slots.Human_human_full_name = Slot(uri=HACKSCHEMA.human_full_name, name="Human_human_full_name", curie=HACKSCHEMA.curie('human_full_name'),
                   model_uri=HACKSCHEMA.Human_human_full_name, domain=Human, range=Optional[str])

slots.Mammal_eye_color = Slot(uri=HACKSCHEMA.eye_color, name="Mammal_eye_color", curie=HACKSCHEMA.curie('eye_color'),
                   model_uri=HACKSCHEMA.Mammal_eye_color, domain=Mammal, range=Optional[str])