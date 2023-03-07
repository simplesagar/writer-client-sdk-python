from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import customizationsresponse as shared_customizationsresponse
from ..shared import failresponse as shared_failresponse
from typing import Optional


@dataclasses.dataclass
class CustomizationsPathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CustomizationsHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CustomizationsRequest:
    headers: CustomizationsHeaders = dataclasses.field()
    path_params: CustomizationsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class CustomizationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    customizations_response: Optional[shared_customizationsresponse.CustomizationsResponse] = dataclasses.field(default=None)
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    