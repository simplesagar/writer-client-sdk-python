"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .contentissue import ContentIssue
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from writer import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProcessedContent:
    issues: Optional[List[ContentIssue]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issues'), 'exclude': lambda f: f is None }})
    

