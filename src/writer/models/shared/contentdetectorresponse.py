from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from writer import utils

class ContentDetectorResponseLabelEnum(str, Enum):
    FAKE = "fake"
    REAL = "real"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ContentDetectorResponse:
    label: ContentDetectorResponseLabelEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    score: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score') }})
    