from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import failresponse as shared_failresponse
from ..shared import subscriptionpublicresponseapi as shared_subscriptionpublicresponseapi
from typing import Optional


@dataclasses.dataclass
class GetSubscriptionDetailsHeaders:
    authorization: str = dataclasses.field(metadata={'header': { 'field_name': 'Authorization', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSubscriptionDetailsRequest:
    headers: GetSubscriptionDetailsHeaders = dataclasses.field()
    

@dataclasses.dataclass
class GetSubscriptionDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    fail_response: Optional[shared_failresponse.FailResponse] = dataclasses.field(default=None)
    headers: Optional[dict[str, list[str]]] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    subscription_public_response_api: Optional[shared_subscriptionpublicresponseapi.SubscriptionPublicResponseAPI] = dataclasses.field(default=None)
    