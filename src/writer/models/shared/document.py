"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .simpleuser import SimpleUser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Optional
from writer import utils

class DocumentAccess(str, Enum):
    PRIVATE = 'private'
    PUBLIC = 'public'
    SHARED = 'shared'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Document:
    access: DocumentAccess = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access') }})
    content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    creation_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creationTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    modification_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modificationTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    organization_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organizationId') }})
    score: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score') }})
    team_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('teamId') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    created_user: Optional[SimpleUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdUser'), 'exclude': lambda f: f is None }})
    modified_user: Optional[SimpleUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedUser'), 'exclude': lambda f: f is None }})
    

