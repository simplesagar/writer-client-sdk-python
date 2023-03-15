from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import contentdetectorrequest as shared_contentdetectorrequest
from ..shared import contentdetectorresponse as shared_contentdetectorresponse
from ..shared import failresponse as shared_failresponse
from typing import Optional


@dataclasses.dataclass
class DetectContentRequest:
    content_detector_request: shared_contentdetectorrequest.ContentDetectorRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    organization_id: Optional[int] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'organizationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DetectContentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    content_detector_responses: Optional[list[shared_contentdetectorresponse.ContentDetectorResponse]] = dataclasses.field(default=None)
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    