"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from .contentdetectorrequest import ContentDetectorRequest
from .contentdetectorresponse import ContentDetectorResponse
from typing import Dict, List, Optional


@dataclasses.dataclass
class DetectContentGlobals:
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class DetectContentRequest:
    content_detector_request: ContentDetectorRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class DetectContentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[ContentDetectorResponse]] = dataclasses.field(default=None)
    

