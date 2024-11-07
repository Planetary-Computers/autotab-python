# RunSkillRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_id** | **str** |  | 
**inputs** | **Dict[str, str]** |  | [optional] 

## Example

```python
from autotab.models.run_skill_request import RunSkillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunSkillRequest from a JSON string
run_skill_request_instance = RunSkillRequest.from_json(json)
# print the JSON string representation of the object
print(RunSkillRequest.to_json())

# convert the object into a dict
run_skill_request_dict = run_skill_request_instance.to_dict()
# create an instance of RunSkillRequest from a dict
run_skill_request_from_dict = RunSkillRequest.from_dict(run_skill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


