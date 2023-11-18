"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .modelcustomization import ModelCustomization
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomizationsResponse:
    customizations: Optional[List[ModelCustomization]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customizations'), 'exclude': lambda f: f is None }})
    
