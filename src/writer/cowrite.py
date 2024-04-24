"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from typing import Optional
from writer import models, utils
from writer._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext

class CoWrite:
    r"""Methods related to CoWrite"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def generate_content(self, generate_template_request: models.GenerateTemplateRequest, team_id: int, organization_id: Optional[int] = None) -> models.GenerateContentResponse:
        r"""Generate content using predefined templates"""
        hook_ctx = HookContext(operation_id='Generate Content', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = models.GenerateContentRequest(
            generate_template_request=generate_template_request,
            team_id=team_id,
            organization_id=organization_id,
        )
        
        _globals = models.GenerateContentGlobals(
            organization_id=self.sdk_configuration.globals.organization_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/cowrite/organization/{organizationId}/team/{teamId}/generate', request, _globals)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, models.GenerateContentRequest, "generate_template_request", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = { **utils.get_query_params(request, _globals), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','401','403','404','4XX','500','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = models.GenerateContentResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type') or '', raw_response=http_res, headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[models.Draft])
                res.draft = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, models.FailResponse)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise models.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise models.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def list_templates(self, team_id: int, template_id: str, organization_id: Optional[int] = None) -> models.ListTemplatesResponse:
        r"""Get a list of your existing CoWrite templates"""
        hook_ctx = HookContext(operation_id='listTemplates', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = models.ListTemplatesRequest(
            team_id=team_id,
            template_id=template_id,
            organization_id=organization_id,
        )
        
        _globals = models.ListTemplatesGlobals(
            organization_id=self.sdk_configuration.globals.organization_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/cowrite/organization/{organizationId}/team/{teamId}/template/{templateId}', request, _globals)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        query_params = { **utils.get_query_params(request, _globals), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','401','403','404','4XX','500','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = models.ListTemplatesResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type') or '', raw_response=http_res, headers=None)
        
        if http_res.status_code == 200:
            res.headers = http_res.headers
            
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[models.TemplateDetailsResponse])
                res.template_details_response = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            res.headers = http_res.headers
            
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, models.FailResponse)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise models.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise models.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise models.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    

