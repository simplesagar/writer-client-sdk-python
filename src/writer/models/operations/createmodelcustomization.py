"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createcustomizationrequest as shared_createcustomizationrequest
from ..shared import failresponse as shared_failresponse
from ..shared import modelcustomization as shared_modelcustomization
from typing import Optional


@dataclasses.dataclass
class CreateModelCustomizationRequest:
    
    create_customization_request: shared_createcustomizationrequest.CreateCustomizationRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateModelCustomizationResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    r"""Bad Request"""
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    model_customization: Optional[shared_modelcustomization.ModelCustomization] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    