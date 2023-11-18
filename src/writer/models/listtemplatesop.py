"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from .templatedetailsresponse import TemplateDetailsResponse
from typing import Dict, List, Optional


@dataclasses.dataclass
class ListTemplatesRequest:
    team_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    template_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'templateId', 'style': 'simple', 'explode': False }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class ListTemplatesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    template_details_response: Optional[TemplateDetailsResponse] = dataclasses.field(default=None)
    
