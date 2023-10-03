"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import briefdocuments as shared_briefdocuments
from enum import Enum
from typing import Optional

class ListTeamDocumentsSortField(str, Enum):
    TITLE = 'title'
    CREATION_TIME = 'creationTime'
    MODIFICATION_TIME = 'modificationTime'
    MODIFIED_BY_ME_TIME = 'modifiedByMeTime'
    OPENED_BY_ME_TIME = 'openedByMeTime'

class ListTeamDocumentsSortOrder(str, Enum):
    ASC = 'asc'
    DESC = 'desc'



@dataclasses.dataclass
class ListTeamDocumentsRequest:
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    search: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search', 'style': 'form', 'explode': True }})
    sort_field: Optional[ListTeamDocumentsSortField] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortField', 'style': 'form', 'explode': True }})
    sort_order: Optional[ListTeamDocumentsSortOrder] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sortOrder', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class ListTeamDocumentsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    brief_documents: Optional[shared_briefdocuments.BriefDocuments] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

