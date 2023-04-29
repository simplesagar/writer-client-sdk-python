"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import customizationsresponse as shared_customizationsresponse
from ..shared import failresponse as shared_failresponse
from typing import Optional


@dataclasses.dataclass
class ListModelCustomizationsRequest:
    
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListModelCustomizationsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    customizations_response: Optional[shared_customizationsresponse.CustomizationsResponse] = dataclasses.field(default=None)
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    r"""Bad Request"""
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    