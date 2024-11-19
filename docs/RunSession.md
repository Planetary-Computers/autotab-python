# RunSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**skill_id** | **str** |  | 
**owner** | **str** |  | 
**created_at** | **datetime** |  | 
**environment** | [**Environment**](Environment.md) |  | 
**start_time** | **datetime** |  | 
**name** | **str** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**state** | [**RunSessionState**](RunSessionState.md) |  | [optional] 
**inputs** | **object** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from autotab.models.run_session import RunSession

# TODO update the JSON string below
json = "{}"
# create an instance of RunSession from a JSON string
run_session_instance = RunSession.from_json(json)
# print the JSON string representation of the object
print(RunSession.to_json())

# convert the object into a dict
run_session_dict = run_session_instance.to_dict()
# create an instance of RunSession from a dict
run_session_from_dict = RunSession.from_dict(run_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


