from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import paginatedresult_fulltermwithuser as shared_paginatedresult_fulltermwithuser
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class FindTermsPathParams:
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    
class FindTermsPartOfSpeechEnum(str, Enum):
    NOUN = "noun"
    VERB = "verb"
    ADVERB = "adverb"
    ADJECTIVE = "adjective"

class FindTermsSortFieldEnum(str, Enum):
    TERM = "term"
    CREATION_TIME = "creationTime"
    MODIFICATION_TIME = "modificationTime"
    TYPE = "type"

class FindTermsSortOrderEnum(str, Enum):
    ASC = "asc"
    DESC = "desc"

class FindTermsTypeEnum(str, Enum):
    APPROVED = "approved"
    BANNED = "banned"
    PENDING = "pending"


@dataclasses.dataclass
class FindTermsQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    part_of_speech: Optional[FindTermsPartOfSpeechEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'partOfSpeech', 'style': 'form', 'explode': True }})
    sort_field: Optional[FindTermsSortFieldEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortField', 'style': 'form', 'explode': True }})
    sort_order: Optional[FindTermsSortOrderEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortOrder', 'style': 'form', 'explode': True }})
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tags', 'style': 'form', 'explode': True }})
    term: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'term', 'style': 'form', 'explode': True }})
    type: Optional[FindTermsTypeEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'type', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class FindTermsHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FindTermsRequest:
    headers: FindTermsHeaders = dataclasses.field()
    path_params: FindTermsPathParams = dataclasses.field()
    query_params: FindTermsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class FindTermsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    paginated_result_full_term_with_user: Optional[shared_paginatedresult_fulltermwithuser.PaginatedResultFullTermWithUser] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    