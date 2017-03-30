# esp_sdk.CloudtraileventsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](CloudtraileventsApi.md#list) | **GET** /v2/alerts/{alert_id}/cloud_trail_events.json | Get a list of Cloud Trail Events
[**show**](CloudtraileventsApi.md#show) | **GET** /v2/cloud_trail_events/{id}.json | Show a single Cloud Trail Event


# **list**
> PaginatedCollection list(alert_id, page=page, include=include)

Get a list of Cloud Trail Events

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CloudtraileventsApi()
alert_id = 56 # int | The ID of the alert to retrieve cloud trail events for
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Cloud Trail Events
    api_response = api_instance.list(alert_id, page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudtraileventsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| The ID of the alert to retrieve cloud trail events for | 
 **page** | [**dict(str, str)**](str.md)| Page Number | [optional] 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> CloudTrailEvent show(id, include=include)

Show a single Cloud Trail Event

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CloudtraileventsApi()
id = 56 # int | Cloud Trail Event Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single Cloud Trail Event
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudtraileventsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Cloud Trail Event Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**CloudTrailEvent**](CloudTrailEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
