from __future__ import annotations
import dataclasses
from ..shared import pagepublicapiresponse as shared_pagepublicapiresponse
from ..shared import pagination as shared_pagination
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaginatedResultPagePublicAPIResponse:
    pagination: shared_pagination.Pagination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination') }})
    total_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalCount') }})
    result: Optional[list[shared_pagepublicapiresponse.PagePublicAPIResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result'), 'exclude': lambda f: f is None }})
    