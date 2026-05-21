# StartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **int** |  | [optional] 
**profile_name** | **str** |  | [optional] 
**profile_url** | **str** |  | [optional] 
**inputs** | **Dict[str, str]** |  | [optional] 
**llm_provider** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**cluster_selector** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**working_dir** | **str** |  | [optional] 
**entrypoint** | **str** |  | [optional] 
**runtime_env_yaml** | **str** |  | [optional] 
**ttl_seconds** | **int** |  | [optional] 
**active_deadline_seconds** | **int** |  | [optional] 
**env_passthrough** | **Dict[str, str]** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from webrobot.models.start_request import StartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartRequest from a JSON string
start_request_instance = StartRequest.from_json(json)
# print the JSON string representation of the object
print(StartRequest.to_json())

# convert the object into a dict
start_request_dict = start_request_instance.to_dict()
# create an instance of StartRequest from a dict
start_request_from_dict = StartRequest.from_dict(start_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


