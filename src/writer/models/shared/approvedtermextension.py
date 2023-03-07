from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ApprovedTermExtension:
    capitalize: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('capitalize') }})
    fix_case: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fixCase') }})
    fix_common_mistakes: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fixCommonMistakes') }})
    term_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('termId') }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    