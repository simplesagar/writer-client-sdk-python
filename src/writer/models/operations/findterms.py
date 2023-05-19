"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import paginatedresult_fulltermwithuser as shared_paginatedresult_fulltermwithuser
from enum import Enum
from typing import Optional

class FindTermsPartOfSpeech(str, Enum):
    NOUN = 'noun'
    VERB = 'verb'
    ADVERB = 'adverb'
    ADJECTIVE = 'adjective'

class FindTermsSortField(str, Enum):
    TERM = 'term'
    CREATION_TIME = 'creationTime'
    MODIFICATION_TIME = 'modificationTime'
    TYPE = 'type'

class FindTermsSortOrder(str, Enum):
    ASC = 'asc'
    DESC = 'desc'

class FindTermsType(str, Enum):
    APPROVED = 'approved'
    BANNED = 'banned'
    PENDING = 'pending'


@dataclasses.dataclass
class FindTermsRequest:
    
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    part_of_speech: Optional[FindTermsPartOfSpeech] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'partOfSpeech', 'style': 'form', 'explode': True }})
    sort_field: Optional[FindTermsSortField] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortField', 'style': 'form', 'explode': True }})
    sort_order: Optional[FindTermsSortOrder] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortOrder', 'style': 'form', 'explode': True }})
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tags', 'style': 'form', 'explode': True }})
    term: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'term', 'style': 'form', 'explode': True }})
    type: Optional[FindTermsType] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'type', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class FindTermsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    r"""Bad Request"""
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    paginated_result_full_term_with_user: Optional[shared_paginatedresult_fulltermwithuser.PaginatedResultFullTermWithUser] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    