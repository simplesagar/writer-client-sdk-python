# billing

## Overview

Methods related to Billing

### Available Operations

* [get_subscription_details](#get_subscription_details) - Get your organization subscription details

## get_subscription_details

Get your organization subscription details

### Example Usage

```python
import writer


s = writer.Writer(
    security=shared.Security(
        api_key="",
    ),
    organization_id=544883,
)


res = s.billing.get_subscription_details()

if res.subscription_public_response_api is not None:
    # handle response
```


### Response

**[operations.GetSubscriptionDetailsResponse](../../models/operations/getsubscriptiondetailsresponse.md)**
