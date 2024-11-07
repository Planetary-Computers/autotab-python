# autotab.SkillApi

All URIs are relative to *https://api.autotab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](SkillApi.md#list) | **GET** /skill/list | List Skills
[**retrieve**](SkillApi.md#retrieve) | **GET** /skill/{id} | Get Skill


# **list**
> List[Skill] list()

List Skills

### Example

* Bearer Authentication (HTTPBearer):

```python
import autotab
from autotab.models.skill import Skill
from autotab.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: HTTPBearer
configuration = autotab.Configuration(
    api_key = os.environ["AUTOTAB_API_KEY"]
)

# Enter a context with an instance of the API client
async with autotab.Client(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autotab.SkillApi(api_client)

    try:
        # List Skills
        api_response = await api_instance.list()
        print("The response of SkillApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillApi->list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Skill]**](Skill.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve**
> Skill retrieve(id)

Get Skill

### Example

* Bearer Authentication (HTTPBearer):

```python
import autotab
from autotab.models.skill import Skill
from autotab.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: HTTPBearer
configuration = autotab.Configuration(
    api_key = os.environ["AUTOTAB_API_KEY"]
)

# Enter a context with an instance of the API client
async with autotab.Client(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autotab.SkillApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Skill
        api_response = await api_instance.retrieve(id)
        print("The response of SkillApi->retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillApi->retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Skill**](Skill.md)

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

