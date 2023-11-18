"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .generationmodelinforesponse import GenerationModelInfoResponse
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerationModelsResponse:
    data: Optional[List[GenerationModelInfoResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    
