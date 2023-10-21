<div align="center">
        <source srcset="https://user-images.githubusercontent.com/6267663/223574357-9a053550-02f9-49f1-b453-1b11db148d7b.svg" media="(prefers-color-scheme: dark)" width="500">
        <img src="https://user-images.githubusercontent.com/6267663/223574369-77805bfe-6d95-44e8-ac48-f9494101e1dc.svg" width="500">
    <h1>Python SDK</h1>
   <p>AI for everyone.</p>
   <a href="https://dev.writer.com/docs"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/writerai/writer-client-sdk-python/releases"><img src="https://img.shields.io/github/v/release/writerai/writer-client-sdk-python?sort=semver&style=for-the-badge" /></a>
  <a href="https://codespaces.new/writerai/writer-client-sdk-python.git/tree/main"><img src="https://github.com/codespaces/badge.svg" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install writerai
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
    api_key="",
    organization_id=496531,
)


res = s.ai_content_detector.detect(content_detector_request=shared.ContentDetectorRequest(
    input='string',
), organization_id=592237)

if res.content_detector_responses is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [ai_content_detector](docs/sdks/aicontentdetector/README.md)

* [detect](docs/sdks/aicontentdetector/README.md#detect) - Content detector api

### [billing](docs/sdks/billing/README.md)

* [get_subscription_details](docs/sdks/billing/README.md#get_subscription_details) - Get your organization subscription details

### [co_write](docs/sdks/cowrite/README.md)

* [generate_content](docs/sdks/cowrite/README.md#generate_content) - Generate content using predefined templates
* [list_templates](docs/sdks/cowrite/README.md#list_templates) - Get a list of your existing CoWrite templates

### [completions](docs/sdks/completions/README.md)

* [create](docs/sdks/completions/README.md#create) - Create completion for LLM model
* [create_model_customization_completion](docs/sdks/completions/README.md#create_model_customization_completion) - Create completion for LLM customization model

### [content](docs/sdks/content/README.md)

* [check](docs/sdks/content/README.md#check) - Check your content against your preset styleguide.
* [correct](docs/sdks/content/README.md#correct) - Apply the style guide suggestions directly to your content.

### [download_the_customized_model](docs/sdks/downloadthecustomizedmodel/README.md)

* [fetch_file](docs/sdks/downloadthecustomizedmodel/README.md#fetch_file) - Download your fine-tuned model (available only for Palmyra Base and Palmyra Large)

### [files](docs/sdks/files/README.md)

* [delete](docs/sdks/files/README.md#delete) - Delete file
* [get](docs/sdks/files/README.md#get) - Get file
* [list](docs/sdks/files/README.md#list) - List files
* [upload](docs/sdks/files/README.md#upload) - Upload file

### [model_customization](docs/sdks/modelcustomization/README.md)

* [create](docs/sdks/modelcustomization/README.md#create) - Create model customization
* [delete](docs/sdks/modelcustomization/README.md#delete) - Delete Model customization
* [get](docs/sdks/modelcustomization/README.md#get) - Get model customization
* [list](docs/sdks/modelcustomization/README.md#list) - List model customizations

### [models](docs/sdks/models/README.md)

* [list](docs/sdks/models/README.md#list) - List available LLM models

### [snippet](docs/sdks/snippet/README.md)

* [delete](docs/sdks/snippet/README.md#delete) - Delete snippets
* [find](docs/sdks/snippet/README.md#find) - Find snippets
* [update](docs/sdks/snippet/README.md#update) - Update snippets

### [styleguide](docs/sdks/styleguide/README.md)

* [get](docs/sdks/styleguide/README.md#get) - Page details
* [list_pages](docs/sdks/styleguide/README.md#list_pages) - List your styleguide pages

### [terminology](docs/sdks/terminology/README.md)

* [add](docs/sdks/terminology/README.md#add) - Add terms
* [delete](docs/sdks/terminology/README.md#delete) - Delete terms
* [find](docs/sdks/terminology/README.md#find) - Find terms
* [update](docs/sdks/terminology/README.md#update) - Update terms

### [user](docs/sdks/user/README.md)

* [list](docs/sdks/user/README.md#list) - List users

### [document](docs/sdks/document/README.md)

* [get](docs/sdks/document/README.md#get) - Get document details
* [list](docs/sdks/document/README.md#list) - List team documents
<!-- End SDK Available Operations -->


<!-- Start Dev Containers -->
# Dev Containers
<div align="left">
    <a href="https://codespaces.new/writerai/writer-client-sdk-python.git/tree/main"><img src="https://github.com/codespaces/badge.svg" /></a>
    
</div>

Experience our SDK in an enhanced sandbox environment. Try it now in **GitHub Codespaces**!

* [Explore Dev Containers](.devcontainer/README.md)
<!-- End Dev Containers -->

<!-- Start Global Parameters -->
# Global Parameters

A parameter is configured globally. This parameter must be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `organizationId` to `547272` at SDK initialization and then you do not have to pass the same value on calls to operations like `detect`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


## Available Globals

The following global parameter is available. The required parameter must be set when you initialize the SDK client.

| Name | Type | Required | Description |
| ---- | ---- |:--------:| ----------- |
| organizationId | int | ✔️ | The organizationId parameter. |



## Example

```python
import writer
from writer.models import operations, shared

s = writer.Writer(
    api_key="",
    organization_id=496531,
)


res = s.ai_content_detector.detect(content_detector_request=shared.ContentDetectorRequest(
    input='string',
), organization_id=592237)

if res.content_detector_responses is not None:
    # handle response
    pass
```
<!-- End Global Parameters -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
