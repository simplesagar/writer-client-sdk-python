from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import completionrequest as shared_completionrequest
from ..shared import completionresponse as shared_completionresponse
from ..shared import failresponse as shared_failresponse
from typing import Optional


@dataclasses.dataclass
class CustomizationCompletionsPathParams:
    customization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customizationId', 'style': 'simple', 'explode': False }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    organization_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CustomizationCompletionsHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CustomizationCompletionsRequest:
    headers: CustomizationCompletionsHeaders = dataclasses.field()
    path_params: CustomizationCompletionsPathParams = dataclasses.field()
    request: shared_completionrequest.CompletionRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CustomizationCompletionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    completion_response: Optional[shared_completionresponse.CompletionResponse] = dataclasses.field(default=None)
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    