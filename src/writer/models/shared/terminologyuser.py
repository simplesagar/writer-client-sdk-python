from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TerminologyUser:
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    full_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fullName'), 'exclude': lambda f: f is None }})
    