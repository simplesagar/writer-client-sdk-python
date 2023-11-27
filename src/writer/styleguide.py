"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from typing import Optional
from writer import models, utils

class Styleguide:
    r"""Methods related to Styleguide"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def get(self, page_id: int) -> models.PageDetailsResponse:
        r"""Page details"""
        request = models.PageDetailsRequest(
            page_id=page_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(models.PageDetailsRequest, base_url, '/styleguide/page/{pageId}', request, self.sdk_configuration.globals)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = models.PageDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res, headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[models.PageWithSectionResponse])
                res.page_with_section_response = out
            else:
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, models.FailResponse)
                out.raw_response = http_res
                raise out
            else:
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise models.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def list_pages(self, limit: Optional[int] = None, offset: Optional[int] = None, status: Optional[models.QueryParamStatus] = None) -> models.ListPagesResponse:
        r"""List your styleguide pages"""
        request = models.ListPagesRequest(
            limit=limit,
            offset=offset,
            status=status,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/styleguide/page'
        headers = {}
        query_params = utils.get_query_params(models.ListPagesRequest, request, self.sdk_configuration.globals)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = models.ListPagesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res, headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[models.PaginatedResultPagePublicAPIResponse])
                res.paginated_result_page_public_api_response = out
            else:
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, models.FailResponse)
                out.raw_response = http_res
                raise out
            else:
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise models.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    