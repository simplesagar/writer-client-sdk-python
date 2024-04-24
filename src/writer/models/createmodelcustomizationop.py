"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from .createcustomizationrequest import CreateCustomizationRequest
from .modelcustomization import ModelCustomization
from typing import Dict, List, Optional


@dataclasses.dataclass
class CreateModelCustomizationGlobals:
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class CreateModelCustomizationRequest:
    create_customization_request: CreateCustomizationRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class CreateModelCustomizationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    model_customization: Optional[ModelCustomization] = dataclasses.field(default=None)
    

