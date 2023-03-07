from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import paginatedresult_pagepublicapiresponse as shared_paginatedresult_pagepublicapiresponse
from enum import Enum
from typing import Optional

class ListPagesStatusEnum(str, Enum):
    LIVE = "live"
    OFFLINE = "offline"


@dataclasses.dataclass
class ListPagesQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    status: Optional[ListPagesStatusEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListPagesHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListPagesRequest:
    headers: ListPagesHeaders = dataclasses.field()
    query_params: ListPagesQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListPagesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    paginated_result_page_public_api_response: Optional[shared_paginatedresult_pagepublicapiresponse.PaginatedResultPagePublicAPIResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    