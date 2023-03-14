import requests as requests_http
from . import utils
from typing import Any, Optional
from writer.models import operations, shared

class DownloadTheCustomizedModel:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str
    _globals: dict[str, dict[str, dict[str, Any]]]

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str, gbls: dict[str, dict[str, dict[str, Any]]]) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        self._globals = gbls
        
    def fetch_file(self, request: operations.FetchCustomizedModelFileRequest) -> operations.FetchCustomizedModelFileResponse:
        r"""Download your fine-tuned model (available only for Palmyra Base and Palmyra Large)
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.FetchCustomizedModelFileRequest, base_url, '/llm/organization/{organizationId}/model/{modelId}/customization/{customizationId}/fetch', request, self._globals)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FetchCustomizedModelFileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/octet-stream'):
                res.fetch_customized_model_file_200_application_octet_stream_binary_string = http_res.content
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out

        return res

    