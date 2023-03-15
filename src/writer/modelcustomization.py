import requests as requests_http
from . import utils
from typing import Any, Optional
from writer.models import operations, shared

class ModelCustomization:
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
        
    def create(self, request: operations.CreateModelCustomizationRequest) -> operations.CreateModelCustomizationResponse:
        r"""Create model customization
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateModelCustomizationRequest, base_url, '/llm/organization/{organizationId}/model/{modelId}/customization', request, self._globals)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "create_customization_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateModelCustomizationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ModelCustomization])
                res.model_customization = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out

        return res

    def delete(self, request: operations.DeleteModelCustomizationRequest) -> operations.DeleteModelCustomizationResponse:
        r"""Delete Model customization
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteModelCustomizationRequest, base_url, '/llm/organization/{organizationId}/model/{modelId}/customization/{customizationId}', request, self._globals)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteModelCustomizationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.delete_model_customization_200_application_json_object = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out

        return res

    def get(self, request: operations.GetModelCustomizationRequest) -> operations.GetModelCustomizationResponse:
        r"""Get model customization
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetModelCustomizationRequest, base_url, '/llm/organization/{organizationId}/model/{modelId}/customization/{customizationId}', request, self._globals)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetModelCustomizationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ModelCustomization])
                res.model_customization = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out

        return res

    def list(self, request: operations.ListModelCustomizationsRequest) -> operations.ListModelCustomizationsResponse:
        r"""List model customizations
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListModelCustomizationsRequest, base_url, '/llm/organization/{organizationId}/model/{modelId}/customization', request, self._globals)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListModelCustomizationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CustomizationsResponse])
                res.customizations_response = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FailResponse])
                res.fail_response = out

        return res

    