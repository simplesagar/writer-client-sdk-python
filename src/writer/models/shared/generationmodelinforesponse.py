from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from writer import utils

class GenerationModelInfoResponseTypeEnum(str, Enum):
    GPT = "GPT"
    INSTRUCT = "Instruct"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenerationModelInfoResponse:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    type: GenerationModelInfoResponseTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    