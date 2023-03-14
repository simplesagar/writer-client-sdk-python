from __future__ import annotations
import dataclasses
from ..shared import generationmodelinforesponse as shared_generationmodelinforesponse
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerationModelsResponse:
    data: Optional[list[shared_generationmodelinforesponse.GenerationModelInfoResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    