"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deleteresponse as shared_deleteresponse
from ..shared import failresponse as shared_failresponse
from typing import Optional


@dataclasses.dataclass
class DeleteSnippetsRequest:
    
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})  
    ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ids', 'style': 'form', 'explode': True }})  
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})  
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Request-ID', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class DeleteSnippetsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    delete_response: Optional[shared_deleteresponse.DeleteResponse] = dataclasses.field(default=None)  
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    r"""Bad Request"""  
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    