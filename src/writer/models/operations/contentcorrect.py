"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import contentrequest as shared_contentrequest
from ..shared import correctionresponse as shared_correctionresponse
from ..shared import failresponse as shared_failresponse
from typing import Optional


@dataclasses.dataclass
class ContentCorrectRequest:
    
    content_request: shared_contentrequest.ContentRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})  
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})  
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})  
    x_request_id: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Request-ID', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class ContentCorrectResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    correction_response: Optional[shared_correctionresponse.CorrectionResponse] = dataclasses.field(default=None)  
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    r"""Bad Request"""  
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    