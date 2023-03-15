<div align="center">
        <source srcset="https://user-images.githubusercontent.com/6267663/223574357-9a053550-02f9-49f1-b453-1b11db148d7b.svg" media="(prefers-color-scheme: dark)" width="500">
        <img src="https://user-images.githubusercontent.com/6267663/223574369-77805bfe-6d95-44e8-ac48-f9494101e1dc.svg" width="500">
    <h1>Python SDK</h1>
   <p>AI for everyone.</p>
   <a href="https://dev.writer.com/docs"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
   <a href="https://github.com/writerai/writer-client-sdk-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/writerai/writer-client-sdk-python/speakeasy_generate.yaml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/writerai/writer-client-sdk-python/releases"><img src="https://img.shields.io/github/v/release/writerai/writer-client-sdk-python?sort=semver&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install writerai-api
```
<!-- End SDK Installation -->

## Authentication

Writer authenticates your API requests using your account’s API keys. If you do not include your key when making an API request, or use one that is incorrect or outdated, Writer returns an error.

Your API keys are available in the account dashboard. We include randomly generated API keys in our code examples if you are not logged in. Replace these with your own or log in to see code examples populated with your own API keys.

<img width="1070" alt="writer-auth" src="https://user-images.githubusercontent.com/6267663/223578295-89087c24-c55a-48bf-b74a-5f057e21e14f.png">

If you cannot see your secret API keys in the Dashboard, this means you do not have access to them. Contact your Writer account owner and ask to be added to their team as a developer.

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
    organization_id=548814,
)


req = operations.DetectContentRequest(
    content_detector_request=shared.ContentDetectorRequest(
        input="example",
    ),
)
    
res = s.ai_content_detector.detect(req)

if res.content_detector_responses is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### ai_content_detector

* `detect` - Content detector api

### billing

* `get_subscription_details` - Get your organization subscription details

### co_write

* `generate_content` - Generate content using predefined templates
* `list_templates` - Get a list of your existing CoWrite templates

### completions

* `create` - Create completion for LLM model
* `create_model_customization_completion` - Create completion for LLM customization model

### content

* `check` - Check your content against your preset styleguide.
* `correct` - Apply the style guide suggestions directly to your content.

### download_the_customized_model

* `fetch_file` - Download your fine-tuned model (available only for Palmyra Base and Palmyra Large)

### files

* `delete` - Delete file
* `get` - Get file
* `list` - List files
* `upload` - Upload file

### model_customization

* `create` - Create model customization
* `delete` - Delete Model customization
* `get` - Get model customization
* `list` - List model customizations

### models

* `list` - List available LLM models

### snippet

* `delete` - Delete snippets
* `find` - Find snippets
* `update` - Update snippets

### styleguide

* `get` - Page details
* `list_pages` - List your styleguide pages

### terminology

* `add` - Add terms
* `delete` - Delete terms
* `find` - Find terms
* `update` - Update terms

### user

* `list` - List users
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
