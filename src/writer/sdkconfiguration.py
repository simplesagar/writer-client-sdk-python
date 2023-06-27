"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass, field
from typing import Any

SERVERS = [
    'https://enterprise-api.writer.com',
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    security_client: requests.Session
    server_url: str = ''
    server_idx: int = 0
    globals: dict[str, dict[str, dict[str, Any]]] = field(default_factory=dict)
    language: str = 'python'
    openapi_doc_version: str = '1.7'
    sdk_version: str = '0.6.0'
    gen_version: str = '2.50.2'

    def get_server_details(self) -> tuple[str, dict[str, str]]:
        if self.server_url:
            return self.server_url.removesuffix('/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
