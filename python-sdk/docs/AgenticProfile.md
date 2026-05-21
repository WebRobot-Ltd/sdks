# AgenticProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**spec** | **str** |  | [optional] 
**spec_yaml** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by_id** | **int** |  | [optional] 

## Example

```python
from webrobot.models.agentic_profile import AgenticProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AgenticProfile from a JSON string
agentic_profile_instance = AgenticProfile.from_json(json)
# print the JSON string representation of the object
print(AgenticProfile.to_json())

# convert the object into a dict
agentic_profile_dict = agentic_profile_instance.to_dict()
# create an instance of AgenticProfile from a dict
agentic_profile_from_dict = AgenticProfile.from_dict(agentic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


