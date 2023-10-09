"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .ai_content_detector import AIContentDetector
from .billing import Billing
from .completions import Completions
from .content import Content
from .cowrite import CoWrite
from .document import Document
from .download_the_customized_model import DownloadTheCustomizedModel
from .files import Files
from .modelcustomization import ModelCustomization
from .models_ import Models
from .sdkconfiguration import SDKConfiguration
from .snippet import Snippet
from .styleguide import Styleguide
from .terminology import Terminology
from .user import User
from writer import utils
from writer.models import shared

class Writer:
    ai_content_detector: AIContentDetector
    r"""Methods related to AI Content Detector"""
    billing: Billing
    r"""Methods related to Billing"""
    co_write: CoWrite
    r"""Methods related to CoWrite"""
    completions: Completions
    r"""Methods related to Completions"""
    content: Content
    r"""Methods related to Content"""
    download_the_customized_model: DownloadTheCustomizedModel
    r"""Methods related to Download the customized model"""
    files: Files
    r"""Methods related to Files"""
    model_customization: ModelCustomization
    r"""Methods related to Model Customization"""
    models: Models
    r"""Methods related to Model"""
    snippet: Snippet
    r"""Methods related to Snippets"""
    styleguide: Styleguide
    r"""Methods related to Styleguide"""
    terminology: Terminology
    r"""Methods related to Terminology"""
    user: User
    r"""Methods related to User"""
    document: Document
    r"""Methods related to document"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 api_key: str,
                 organization_id: int = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param api_key: The api_key required for authentication
        :type api_key: str
        :param organization_id: Configures the organization_id parameter for all supported operations
        :type organization_id: int
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        
        security_client = utils.configure_security_client(client, shared.Security(api_key = api_key))
        
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx, {
            'parameters': {
                'queryParam': {
                },
                'pathParam': {
                    'organization_id': organization_id,
                },
            },
        }, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.ai_content_detector = AIContentDetector(self.sdk_configuration)
        self.billing = Billing(self.sdk_configuration)
        self.co_write = CoWrite(self.sdk_configuration)
        self.completions = Completions(self.sdk_configuration)
        self.content = Content(self.sdk_configuration)
        self.download_the_customized_model = DownloadTheCustomizedModel(self.sdk_configuration)
        self.files = Files(self.sdk_configuration)
        self.model_customization = ModelCustomization(self.sdk_configuration)
        self.models = Models(self.sdk_configuration)
        self.snippet = Snippet(self.sdk_configuration)
        self.styleguide = Styleguide(self.sdk_configuration)
        self.terminology = Terminology(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
        self.document = Document(self.sdk_configuration)
    