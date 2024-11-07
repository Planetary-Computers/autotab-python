# autotab.RunApi

All URIs are relative to *https://api.autotab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](RunApi.md#cancel) | **POST** /run/{id}/cancel | Cancel
[**list**](RunApi.md#list) | **GET** /run/list | List Runs
[**retrieve**](RunApi.md#retrieve) | **GET** /run/{id} | Retrieve
[**start**](RunApi.md#start) | **POST** /run/ | Start


# **cancel**
> str cancel(id)

Cancel

### Example

* Bearer Authentication (HTTPBearer):

```python
import autotab
from autotab.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: HTTPBearer
configuration = autotab.Configuration(
    api_key = os.environ["AUTOTAB_API_KEY"]
)

# Enter a context with an instance of the API client
async with autotab.Client(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autotab.RunApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel
        api_response = await api_instance.cancel(id)
        print("The response of RunApi->cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> List[RunSession] list(skill_id=skill_id, state_filter=state_filter)

List Runs

### Example

* Bearer Authentication (HTTPBearer):

```python
import autotab
from autotab.models.run_session import RunSession
from autotab.models.run_session_state import RunSessionState
from autotab.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: HTTPBearer
configuration = autotab.Configuration(
    api_key = os.environ["AUTOTAB_API_KEY"]
)

# Enter a context with an instance of the API client
async with autotab.Client(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autotab.RunApi(api_client)
    skill_id = 'skill_id_example' # str | The skill to list run sessions for (optional)
    state_filter = [autotab.RunSessionState()] # List[RunSessionState] | The state filter to list run sessions for (optional)

    try:
        # List Runs
        api_response = await api_instance.list(skill_id=skill_id, state_filter=state_filter)
        print("The response of RunApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | **str**| The skill to list run sessions for | [optional] 
 **state_filter** | [**List[RunSessionState]**](RunSessionState.md)| The state filter to list run sessions for | [optional] 

### Return type

[**List[RunSession]**](RunSession.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve**
> RunSessionWithData retrieve(id)

Retrieve

### Example

* Bearer Authentication (HTTPBearer):

```python
import autotab
from autotab.models.run_session_with_data import RunSessionWithData
from autotab.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: HTTPBearer
configuration = autotab.Configuration(
    api_key = os.environ["AUTOTAB_API_KEY"]
)

# Enter a context with an instance of the API client
async with autotab.Client(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autotab.RunApi(api_client)
    id = 'id_example' # str | 

    try:
        # Retrieve
        api_response = await api_instance.retrieve(id)
        print("The response of RunApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RunSessionWithData**](RunSessionWithData.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> RunSession start(run_skill_request)

Start

### Example

* Bearer Authentication (HTTPBearer):

```python
import autotab
from autotab.models.run_session import RunSession
from autotab.models.run_skill_request import RunSkillRequest
from autotab.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: HTTPBearer
configuration = autotab.Configuration(
    api_key = os.environ["AUTOTAB_API_KEY"]
)

# Enter a context with an instance of the API client
async with autotab.Client(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autotab.RunApi(api_client)
    run_skill_request = autotab.RunSkillRequest() # RunSkillRequest | 

    try:
        # Start
        api_response = await api_instance.start(run_skill_request)
        print("The response of RunApi->start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunApi->start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_skill_request** | [**RunSkillRequest**](RunSkillRequest.md)|  | 

### Return type

[**RunSession**](RunSession.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

