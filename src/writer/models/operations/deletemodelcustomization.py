"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class DeleteModelCustomizationRequest:
    customization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customizationId', 'style': 'simple', 'explode': False }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class DeleteModelCustomization200ApplicationJSON:
    pass



@dataclasses.dataclass
class DeleteModelCustomizationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_model_customization_200_application_json_object: Optional[DeleteModelCustomization200ApplicationJSON] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

