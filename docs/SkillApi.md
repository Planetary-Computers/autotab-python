# autotab.SkillApi

All URIs are relative to *https://api.autotab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_skills**](SkillApi.md#list_skills) | **GET** /skill/list | List
[**retrieve_skill**](SkillApi.md#retrieve_skill) | **GET** /skill/{id} | Retrieve


# **list_skills**
> List[Skill] list_skills()

List

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
        # List
        api_response = await api_instance.list_skills()
        print("The response of SkillApi->list_skills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillApi->list_skills: %s\n" % e)
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

# **retrieve_skill**
> Skill retrieve_skill(id)

Retrieve

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
        # Retrieve
        api_response = await api_instance.retrieve_skill(id)
        print("The response of SkillApi->retrieve_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillApi->retrieve_skill: %s\n" % e)
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

