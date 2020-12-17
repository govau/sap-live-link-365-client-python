# saplivelink365.EmailApi

All URIs are relative to *https://livelink.sapmobileservices.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email_using_post1**](EmailApi.md#send_email_using_post1) | **POST** /email/send | Send email message


# **send_email_using_post1**
> EmailChannelResponse send_email_using_post1(body)

Send email message

Send an email message to one or more email addresses specified as recipients.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import saplivelink365
from saplivelink365.rest import ApiException
from pprint import pprint
configuration = saplivelink365.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://livelink.sapmobileservices.com/api
configuration.host = "https://livelink.sapmobileservices.com/api"
# Create an instance of the API class
api_instance = saplivelink365.EmailApi(saplivelink365.ApiClient(configuration))
body = saplivelink365.EmailRequest() # EmailRequest | 

try:
    # Send email message
    api_response = api_instance.send_email_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->send_email_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailRequest**](EmailRequest.md)|  | 

### Return type

[**EmailChannelResponse**](EmailChannelResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

